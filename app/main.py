# Data Handling
import pickle
import numpy as np
import pandas as pd
from pydantic import BaseModel

# Server
import uvicorn
from fastapi import FastAPI

# Modeling
import lightgbm

app = FastAPI()

# Initialize files
# clf = pickle.load(open('data/model.pickle', 'rb'))
# enc = pickle.load(open('data/encoder.pickle', 'rb'))
#
# # Load data and save indices of columns
# df = pd.read_csv("../notebooks/data.csv")
# features = df.drop('left', 1).columns
# features = pickle.load(open('data/features.pickle', 'rb'))


class Data(BaseModel):
    satisfaction_level: float
    last_evaluation: float
    number_project: float
    average_montly_hours: float
    time_spend_company: float
    Work_accident: float
    promotion_last_5years: float
    sales: str
    salary: str


@app.post("/predict")
def predict(data: Data):
    # Extract data in correct order
    data_dict = data.dict()

    return {"prediction": data_dict[0]}