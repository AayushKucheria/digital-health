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
import upload_data

models.database.Base.metadata.create_all(bind=engine)

app = FastAPI()
print(models.database.Base.metadata)

# Allow communication with JS backend 

# origins = [
#     "http://localhost:3000"
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:8081"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


## I am trying work work on a short example here ....patient_id might need to be str
@app.get("/patients/{patient_id}", response_model=schemas.Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient_by_id(db, patient_id=patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="User not found")
    print(patient)
    return patient


# Copied from read_patient()
@app.get("/patients/{patient_id}", response_model=schemas.Patient)
def read_patient_results_all(patient_id: int, db: Session = Depends(get_db)):
    results = crud.get_results_by_patient_id(db, patient_id)
    if results is None:
        raise HTTPException(status_code=404, detail="No results yet.")
    print(results)
    return results


# Copied from read_patient()
@app.get("/patients/{patient_id}", response_model=schemas.Patient)
def read_patient_results_latest(patient_id: int, db: Session = Depends(get_db)):
    results = crud.get_last_result_by_patient_id(db, patient_id)
    if results is None:
        raise HTTPException(status_code=404, detail="No results yet.")
    print(results)
    return results


# Create a patient in database when a "Patient" query has been sent
@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient_by_id(db, patient_id=patient.id)
    print('db_patient', db_patient)
    if db_patient:
        raise HTTPException(status_code=400, detail="ID already registered")
    return crud.create_patient(db=db, patient=patient)


# Upload csv files for a specific patient by clicking button from the patient's page?
# Param: id or name to get the correct files
# Returns true if successful false if not
@app.post("/patients/{patient_id}", response_model=List[schemas.Patient])
def upload_csv(patient_id: str, db: Session = Depends(get_db)):
    print("Method executing")
    return upload_data.start()


@app.post("/patients/{patient_id}", response_model=List[schemas.Patient])
def k_means(patient_id: str, db: Session = Depends(get_db)):
    print("K-Means executing")
    upload_data.start()  # Replace with k_means.start()
    #  return results from database


@app.post("/patients/{patient_id}", response_model=List[schemas.Patient])
def deep_learning(patient_id: str, db: Session = Depends(get_db)):
    print("Deep Learning executing")
    upload_data.start()  # Replace with dl.start()
    #  return results from database
