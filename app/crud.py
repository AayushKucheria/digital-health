# Reusable functions to interact with data
# in database
# CRUD = Create Read Update Delete

from sqlalchemy.orm import Session
from app import models, schemas

### Reading Data ###

# Replace User._ with anything else to get user by _
def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


### Creating data ###

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(sex=patient.sex, age=patient.age)
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