
import os
import psycopg2
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import crud, models, schemas

models.database.Base.metadata.create_all(bind=engine)


app = FastAPI()

# DATABASE_URL = os.environ['postgres://qrutnlncgfznek:ca0781860fbb93e669ec0c0ca760ad32ae1c84d5e1580f6bc11aa4ec3c6d8764@ec2-34-197-188-147.compute-1.amazonaws.com:5432/db2rqfi8hqb9l5']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#
# @app.get("/")
# async def main():
#     return {"prediction": "Hello World"}

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db, id = patient.id)
    if db_patient:
        raise HTTPException(status_code=400, detail = "ID already registered")
    return crud.create_patient(db=db, patient=patient)

@app.get("/patients/", response_model=List[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = crud.get_patients(db, skip=skip, limit=limit)
    return patients

