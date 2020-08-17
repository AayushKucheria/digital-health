# from tslearn.clustering import TimeSeriesKMeans
import numpy as np
import crud
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy.sql import select

def get_session_data(p_id: int):
    db: Session = SessionLocal()
    latest_session = crud.get_latest_session_table_by_id(db, p_id)
    print(crud.get_table_data(db, latest_session))


def knn(p_id):
    test: list[np.ndarray[np.ndarray[np.int]]]
    get_session_data(p_id)
    # model = TimeSeriesKMeans.from_json('res/knn_model.txt')
    # model
    # pred = model.predict(test)
    # a = np.zeros((320,), dtype=int)
    # b = np.ones((80,), dtype=int)
    # true = np.concatenate([a, b])
    # # confusion_matrix(true, pred)
    # return pred


if __name__ == "__main__":
    knn(17)