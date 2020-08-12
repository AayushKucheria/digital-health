'''
CRUD = Create Read Update Delete
Add necessary sql functions here to use throughout the project.
'''

import pandas as pd
from sqlalchemy import MetaData, Table, Column, Integer, Float, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, inspector


# TODO Add security check fastapi

### Reading Data ###

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()


def get_patient_by_name(db: Session, patient_name: str):
    return db.query(models.Patient).filter(models.Patient.name == patient_name).first()


def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()


def get_tables_by_name(db: Session):
    return inspector.get_table_names()

def get_session_tables(db: Session):
    allTables = get_tables_by_name(db)
    print("All tables:")
    print(allTables)
    print("Filtered tables:")
    a = [k for k in allTables if '_' in k]
    print(a)
    return a


### Creating data ###

# TODO:
# Edit patient
# Manual ID SOLVED
# Get only emg and eeg tables (filter patients and datasets)
def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(age=patient.age, sex=patient.sex, name=patient.name, id=patient.id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


# TODO: Ability to specify number of channels? Or hardcode it
def create_emg_table(db: Session, tablename: String):
    metadata = MetaData()
    # name = String("{}_{}_{}".format(type, id, session))
    name = "emg_" + tablename
    table = Table(name, metadata,
                  Column('timestamp', Integer, primary_key=True),
                  Column('Channel 1', Float, nullable=False),
                  Column('Channel 2', Float, nullable=False),
                  Column('Channel 3', Float, nullable=False),
                  Column('Channel 4', Float, nullable=False))
    metadata.create_all(engine)
    return name


# Add csv data to specified table
def send_data(db: Session, tablename: str, csv_path: str):
    print("Sending data...")
    df = pd.read_csv(csv_path)
    conn = db.connection()
    df.to_sql(tablename, con=conn, if_exists='replace', index=False)
    try:
        db.commit()
        print("Data sent successfully.")
    except IntegrityError as e:
        raise ArithmeticError("Duplicate record exists")

