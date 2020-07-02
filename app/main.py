# Data Handling
import pickle
import numpy as np
import pandas as pd
from pydantic import BaseModel

# Server
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"prediction": "Hello World"}