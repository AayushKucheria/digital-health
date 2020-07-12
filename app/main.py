'''
Gets the local server running
Run from uvicorn main:app
'''

from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.database.Base.metadata.create_all(bind=engine)

app = FastAPI()
print(models.database.Base.metadata)


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

