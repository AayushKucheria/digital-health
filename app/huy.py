import numpy as np
import tensorflow as tf
import pandas as pd

import app.crud as crud
from sqlalchemy.orm import Session
from app.database import SessionLocal

import app.models as models

m_id = 1
db: Session = SessionLocal()


# Original methods from DL Notebook
# method run input as size (4097x??)
def testAug1(testSet):
    Divide1 = []
    for m in range(5):
        for k in range(4):
            divide1 = testSet.iloc[:, m][k * 1024:1024 + k * 1024].values.flatten()
            Divide1.append(divide1)
    CUT1 = []
    for r in Divide1:
        for p in range(3):
            chop1 = r[p * 256:512 + 256 * p]
            CUT1.append(chop1)
    return pd.DataFrame(tf.keras.utils.normalize(np.array(CUT1).T))


def load_huy_model(exists: bool, input, p_id: int, s_id: int):
    print("---------DL---------")
    if exists:
        print("Returning last result")
        print(input)
        return input  # crud.get_last_result(db, p_id, m_id)
    else:
        print("Running Model")
        testInstance = testAug1(input)
        Xtest = np.expand_dims(testInstance.T, 2)
        model = tf.keras.models.load_model("./")
        res = model.predict(Xtest)
        res = np.where(res > 0.5, 1, 0).flatten()
        counts = np.bincount(res)
        final = np.argmax(counts)

        res = models.Result(session_id=int(s_id), patient_id=int(p_id), result=int(final), model_id=m_id)
        return crud.create_patient_result(db, res)


# Get table from database ##
def get_session_data(p_id: int):
    session = crud.get_latest_session_table_by_id(db, p_id)
    s_id = session.split('_')[3]
    exists = crud.is_result_present(db, p_id, s_id, m_id)
    print("Getting Session Data")
    print("Exists: ", exists)
    if exists:
        return exists, [], s_id
    else:  # print(crud.get_table_data(db, latest_session))
        return exists, crud.get_table_data(db, session), s_id


# Picking only 4096 rows from data to insert into DL Model
def edit_data(p_id: int):
    exists, raw_session_table, s_id = get_session_data(p_id)
    print("----Editing Data----")
    if exists:
        print("Returning last result")
        return True, crud.get_last_result(db, p_id, m_id), p_id, s_id
    else:
        # Read column names from file
        data = []
        count = 0
        for row in raw_session_table:
            row_without_timestamp = list()
            for i in range(len(row)):
                if i > 0:
                    row_without_timestamp.append(row[i])
            if count <= 4096:
                data.append(row_without_timestamp)
                count += 1
                continue
            break

        data = (np.array(data))
        data = pd.DataFrame(data)
        print(data)
        print(data.shape)

        print("Returning edited data")
        return False, data, p_id, s_id


def start(pat_id: int):
    exists, data, p_id, s_id = edit_data(pat_id)
    return load_huy_model(exists, data, p_id, s_id)


if __name__ == "__main__":
    # Test Run
    exists, data, p_id, s_id = edit_data(17)
    # load_huy_model(edit_data(17))
