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


# Get patient from id
@app.get("/patients/{patient_id}", response_model=schemas.Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient_by_id(db, patient_id=patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="User not found")
    print(patient)
    return patient


# Get patient result
@app.get("/patients/{p_id}/result", response_model=schemas.Result)
def read_result(patient_id: int, db: Session = Depends(get_db)):
    result = crud.get_last_result_by_patient_id(db, p_id=patient_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User session result not found")
    print(result)
    return result


# Create a patient in database when a "Patient" query has been sent
@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient_by_id(db, patient_id=patient.id)
    print('db_patient', db_patient)
    if db_patient:
        raise HTTPException(status_code=400, detail="ID already registered")
    return crud.create_patient(db=db, patient=patient)


### Creating result ####
# @app.post("/patients/{patient_id}/results", response_model=schemas.Result)
# def create_patient_result(result:schemas.ResultCreate, patient_id: int, db: Session = Depends(get_db)):
#     print ("Reach to create patient result")
#     return crud.create_patient_result(db=db, result=result, patient_id=result.patient_id)

# Upload csv files for a specific patient by clicking button from the patient's page?
# Param: id or name to get the correct files
# Returns true if successful false if not
@app.post("/patients/{patient_id}", response_model=List[schemas.Patient])
def upload_csv(patient_id: int, db: Session = Depends(get_db)):
    print("Method executing")
    # return upload_data.start()


@app.get("/patients/{patient_id}/kmean", response_model=schemas.Result)
def k_means(patient_id: int, db: Session = Depends(get_db)):
    # ai.knn(patient_id)
    result = crud.get_last_result_by_patient_id(db, p_id=patient_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User session result not found")
    print(result.result)
    # result = { "patient_id": 17, "model_id": 0, "result": 0, "session_id":10}
    return result
    


@app.get("/patients/{patient_id}/dlearn", response_model=List[schemas.Patient])
def deep_learning(patient_id: int, db: Session = Depends(get_db)):
    # huy.load_huy_model(huy.edit_data(patient_id))
    result = crud.get_last_result_by_patient_id(db, p_id=patient_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User session result not found")
    print(result)
    return result

    #  return results from database
