'''
CRUD = Create Read Update Delete
Add necessary sql functions here to use throughout the project.
'''

from sqlalchemy import MetaData, Table, Column, Integer, Float, String
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, inspector


### Reading Data ###

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def get_patient_by_name(db: Session, patient_name: str):
    return db.query(models.Patient).filter(models.Patient.name == patient_name).first()

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_tables_by_name(db: Session):
    return inspector.get_table_names()


### Creating data ###

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(age=patient.age, sex=patient.sex, name=patient.name)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def create_patient_item(db: Session, item: schemas.ItemCreate, mpatient_id: int):
    db_item = models.Item(**item.dict(), patient_id=mpatient_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# TODO: 4 channels here since the demo works with 4 channels.
# Change according to what you're using.
def create_emg_table(db: Session, tablename: String):
    metadata = MetaData()
    table = Table("EMG_" + tablename, metadata,
                  Column('timestamp', Integer, primary_key=True),
                  Column('Channel 1',Float, nullable=False),
                  Column('Channel 2',Float, nullable=False),
                  Column('Channel 3',Float, nullable=False),
                  Column('Channel 4',Float, nullable=False))
    metadata.create_all(engine)
