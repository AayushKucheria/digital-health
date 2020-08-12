'''
Communication b/w frontend and backend.
Run local server command: uvicorn main:app
'''

from typing import List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.database.Base.metadata.create_all(bind=engine)

app = FastAPI()
print(models.database.Base.metadata)

# Allow communication with JS backend 

origins = [
    "http://localhost:3000"
    "http://localhost",
    "http://localhost:8081"
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
    return patients


# Create a patient in database when a "Patient" query has been sent
@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient_by_id(db, patient_id=patient.id)
    print ('db_patient',db_patient)
    if db_patient:
        raise HTTPException(status_code=400, detail="ID already registered")
    return crud.create_patient(db=db, patient=patient)
