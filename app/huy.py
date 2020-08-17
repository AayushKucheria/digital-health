import tensorflow as tf
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
  for m in range(10):
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

## Get table from database ## 
    ## Question: in CSV still? 
def get_session_data(p_id: int):
    db: Session = SessionLocal()
    latest_session = crud.get_latest_session_table_by_id(db, p_id)
    print(crud.get_table_data(db, latest_session))
    return crud.get_table_data(db, latest_session)

## If CVS 
def edit_data(p_id: int):
    raw_session_table = get_session_data(p_id)

    # Read column names from file
    cols = list(pd.read_csv(raw_session_table, nrows =1)) # OR 2 if the metadata of that table isn't dropped
    print(cols)

    df= pd.read_csv(raw_session_table, usecols =[i for i in cols if i != 'Timestamp'], skiprows=2, nrows=4099)
    return df

if __name__ == "__main__":
    load_huy_model(edit_data(17))




