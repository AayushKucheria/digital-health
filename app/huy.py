import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import pandas as pd
import pandas.testing as tm
import os
import sklearn_pandas
from sklearn.model_selection import train_test_split

import crud
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy.sql import select
import models

m_id = 1
db: Session = SessionLocal()


## Original methods from Huy ##
# method run input as size (4097x??)
def testAug1(testSet):
    Divide1 = []
    for m in range(5):
        for k in range(4):
            divide1 = testSet.iloc[:, m][k * 1024:1024 + k * 1024].values.flatten()
            Divide1.append(divide1)
    divX1 = pd.DataFrame(np.array(Divide1))
    CUT1 = []
    for r in Divide1:
        for p in range(3):
            chop1 = r[p * 256:512 + 256 * p]
            CUT1.append(chop1)
    return pd.DataFrame(tf.keras.utils.normalize(np.array(CUT1).T))


def load_huy_model(exists: bool, input, p_id: int, s_id: int):
    print("---------HUY---------")
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
# Question: in CSV still?
def get_session_data(p_id: int):
    session = crud.get_latest_session_table_by_id(db, p_id)
    s_id = session.split('_')[3]
    exists = crud.is_result_present(db, p_id, s_id, m_id)
    print("Getting Session Data")
    print("Exists: ", exists)
    if exists:
        return exists, [], s_id
    else: # print(crud.get_table_data(db, latest_session))
        return exists, crud.get_table_data(db, session), s_id


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
                if (i > 0):
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

        # data = pd.DataFrame(data=data[0:,0:].T)
        # data =  pd.DataFrame(data=data[1:,0:])
        # or
        # data =  pd.DataFrame(data=data[0:,1:])
        # and
        # data =  pd.DataFrame(data=data[1:,1:])
        print("Returning edited data")
        return False, data, p_id, s_id


def start(pat_id: int):
    exists, data, p_id, s_id = edit_data(pat_id)
    return load_huy_model(exists, data, p_id, s_id)


if __name__ == "__main__":
    exists, data, p_id, s_id = edit_data(17)
    # load_huy_model(edit_data(17))
