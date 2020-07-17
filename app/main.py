'''
Gets the local server running
Run from uvicorn main:app
'''

from typing import List

from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
from models import Patient

models.database.Base.metadata.create_all(bind=engine)

app = FastAPI()
print(models.database.Base.metadata)

# Allow communication with JS backend 

origins = [
    "http://localhost:3000"
    "http://localhost",
    "http://172.20.10.6:8081",
    "http://172.20.10.6:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()  # Creating a session
    try:
        yield db
    finally:
        db.close()


# Get all patients from database
@app.get("/patients/", response_model=List[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = crud.get_patients(db, skip=skip, limit=limit)
    print(patients)
    return patients


# Create a patient in database when a "Patient" query has been sent
@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db, patient_id=patient.id)
    if db_patient:
        raise HTTPException(status_code=400, detail="ID already registered")
    return crud.create_patient(db=db, patient=patient)

# @app.post("/upload/")
# def send_data(tablename: str, csv_path: str, db: Session = Depends(get_db)):



