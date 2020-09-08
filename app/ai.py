from tslearn.clustering import TimeSeriesKMeans
import numpy as np
import app.crud as crud
# import crud
from sqlalchemy.orm import Session
from app.database import SessionLocal
# from database import SessionLocal
from sklearn.metrics import confusion_matrix
import app.models as models
# import models

db: Session = SessionLocal()
m_id = 0

def get_session_data(p_id: int):
    global db, m_id
    session = crud.get_latest_session_table_by_id(db, p_id)
    print("------------------------KNN-------------------------")
    print("Session: ", session)
    s_id = session.split('_')[3]
    # latest_session = crud.get_dl_session_table(db, p_id)
    exists = crud.is_result_present(db, p_id, s_id, m_id)
    print("Result Exists: ", exists)
    # latest_session_db_id = crud.get_last_result_by_patient_id(db, p_id).session_id
    # if latest_session_db_id == int(latest_session.split('_')[3]):
    #     print("Result for session %s already present as %s".format(latest_session.split('_')[3], str(latest_session_db_id)))
    #     return False, np.array(0)
    if exists:
        return exists, np.array(0)
    else:
        # print("Result for session %s not present, latest = %s" % (s_id.split('_')[3], str(latest_session_db_id)))
        initial_data = crud.get_table_data(db, session)
        test = []
        for row in initial_data:
            temp = []
            for elem in row[1:]:
                temp.append([int(elem)])
            test.append(np.asarray(temp))

        a = np.array(test)
        return False, a


def knn(p_id):
    # get_session_data(p_id)
    (exists, test) = get_session_data(p_id)
    if not exists:
        print("Running KNN Model")
        s_id = crud.get_latest_session_table_by_id(db, p_id).split('_')[3]
        model = TimeSeriesKMeans.from_json('res/knn_model.txt')
        pred = model.predict(test)

        leng = len(test)
        more = int(0.8 * leng)
        less = int(0.2 * leng)
        if more + less < leng:
            more += 1
        elif more + less > leng:
            more -= 1
        a = np.zeros((more,), dtype=int)
        b = np.ones((less,), dtype=int)
        true = np.concatenate([a, b])

        res = 0
        if (pred == 0).sum() < (pred == 1).sum():
            res = 1
        print("-----------------------------")
        print(exists)
        print("-----------------------------")
        res = models.Result(session_id=int(s_id), patient_id=int(p_id), result=int(res), model_id=0)
        return crud.create_patient_result(db, res)
    else:
        return crud.get_last_result(db, p_id, m_id)
        # return crud.get_last_result_by_patient_id(db, p_id)
    print(pred)
    print(confusion_matrix(true, pred))


if __name__ == "__main__":
    knn(17)
