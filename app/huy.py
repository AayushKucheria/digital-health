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

## Original methods from Huy ##
#method run input as size (4097x??) 
def testAug1(testSet):
  Divide1 = []
  for m in range(5):
    for k in range(4):
      divide1 = testSet.iloc[:,m][k*1024:1024+k*1024].values.flatten()
      Divide1.append(divide1)
  divX1 = pd.DataFrame(np.array(Divide1))
  CUT1 = []
  for r in Divide1:
    for p in range(3):
      chop1 = r[p*256:512+256*p]
      CUT1.append(chop1)
  return pd.DataFrame(tf.keras.utils.normalize(np.array(CUT1).T))

def load_huy_model(input):
  testInstance = testAug1(input)
  Xtest = np.expand_dims(testInstance.T, 2)
  model = tf.keras.models.load_model("./")
  res = model.predict(Xtest)
  res = np.where(res > 0.5, 1, 0).flatten()
  counts = np.bincount(res)
  print(np.argmax(counts))
  return

# Get table from database ## 
    # Question: in CSV still? 
def get_session_data(p_id: int):
    db: Session = SessionLocal()
    latest_session = crud.get_latest_session_table_by_id(db, p_id)
    # print(crud.get_table_data(db, latest_session))
    return crud.get_table_data(db, latest_session)

# def get_session_data(p_id: int):
#     db: Session = SessionLocal()
#     latest_session = crud.get_latest_session_table_by_id(db, p_id)
#     initial_data = crud.get_table_data(db, latest_session)
#     test = []
#     for row in initial_data:
#         temp = []
#         for elem in row[1:4080]:
#             temp.append(int(elem))
#         test.append(np.asarray(temp))

#     a = np.array(test)
#     return a

## 
def edit_data(p_id: int):
    raw_session_table = get_session_data(p_id)

    # Read column names from file
    data = []
    count = 0
    for row in raw_session_table:
      row_without_timestamp = list()
      for i in range (len(row)):
        if (i > 0): 
          row_without_timestamp.append(row[i])
      if count <= 4096: 
          data.append(row_without_timestamp)
          count += 1
          continue
      break

    data = (np.array(data))
    data = pd.DataFrame(data)
    print (data)
    print(data.shape)
    
    # data = pd.DataFrame(data=data[0:,0:].T)
    # data =  pd.DataFrame(data=data[1:,0:])
    # or
    # data =  pd.DataFrame(data=data[0:,1:])
    # and
    # data =  pd.DataFrame(data=data[1:,1:])

    return data

if __name__ == "__main__":
    load_huy_model(edit_data(17))




