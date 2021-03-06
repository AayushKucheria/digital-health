'''
CRUD = Create Read Update Delete
Add necessary sql functions here to use throughout the project.
'''

import pandas as pd
from sqlalchemy import MetaData, Table, Column, Integer, Float, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

import app.models as models
import app.schemas as schemas
from app.database import engine, inspector, metadata
# import models
# import schemas
# from database import engine, inspector, metadata



# TODO Add security check fastapi

### Reading Data ###

def get_patient_by_id(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()


def get_patient_by_name(db: Session, patient_name: str):
    return db.query(models.Patient).filter(models.Patient.name == patient_name).first()


def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()  # .all() returns the object as a list


def get_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Result).offset(skip).limit(limit).all()


def get_results_by_patient_id(db: Session, p_id: int):
    return db.query(models.Result).filter(models.Result.patient_id == p_id).all()


def get_last_result_by_patient_id(db: Session, p_id: int):
    # return get_results_by_patient_id(db, p_id).last()
    return max(db.query(models.Result).filter(models.Result.patient_id == p_id).all(), key=lambda x: int(x.session_id))


def get_last_result(db: Session, p_id: int, m_id: int):
    return max(
        db.query(models.Result).filter(models.Result.patient_id == p_id).filter(models.Result.model_id == m_id).all(),
        key=lambda x: int(x.session_id))


def is_result_present(db: Session, p_id: int, s_id: int, m_id: int):
    a = db.query(models.Result).filter(
        models.Result.model_id == m_id).filter(
        models.Result.patient_id == p_id).filter(
        models.Result.session_id == s_id).all()
    if len(a) < 1:
        return False
    else:
        return True


def get_tables_by_name(db: Session):
    """
    Get all table names from database

    :param db: Current database session
    :return: List[String] of all table names
    """
    return inspector.get_table_names()


def get_table_data(db: Session, name: str):
    my_table = Table(name, metadata, autoload=True, autoload_with=db)
    s = select([my_table])
    result = engine.execute(s)
    temp = []
    for row in result:
        temp.append(row)
    return temp


# Get only emg and eeg tables (filter patients and datasets)
def get_session_tables(db: Session):
    """
    Get only emg and eeg sessions names from database.

    :param db: Current database session
    :return: List[String] of emg and eeg table names
    """
    allTables = get_tables_by_name(db)
    a = [k for k in allTables if 'session' in k]
    return a


def get_session_tables_by_id(db: Session, p_id: int):
    patient_sessions = get_session_tables(db)
    a = [k for k in patient_sessions if str(p_id) in k]
    return a


def get_latest_session_table_by_id(db: Session, p_id: int):
    patient_sessions = get_session_tables_by_id(db, p_id)
    patient_sessions.sort(key=lambda x: int(x.split('_')[3]))
    return patient_sessions[-1]


def get_dl_session_table(db: Session, p_id: int):
    sessions = get_session_tables_by_id(db, p_id)
    patient_sessions = [i for j, i in enumerate(sessions) if sessions[j] == "session_eeg_17_5"]
    return patient_sessions[0]


### Creating data ###

# TODO:
# Edit patient
def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(age=patient.age, sex=patient.sex, name=patient.name, id=patient.id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


### Creating result ###
def create_patient_result(db: Session, result: schemas.ResultCreate):
    db_result = result
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

### Delete patient ###
def delete_patient_by_id(db: Session, patient_id: int):
    db.query(models.Patient).filter(models.Patient.id == patient_id).delete()
    try:
        db.commit()
        print ("Patient is deleted")
        return True
    except InvalidRequestError:
        db.session.rollback()
        print ("Patient is NOT deleted")
        raise InvalidRequestError

## REPLACED WITH send_data() for a general usecase
# def create_emg_table(db: Session, tablename: String):
#     metadata = MetaData()
#     # name = String("{}_{}_{}".format(type, id, session))
#     name = "emg_" + tablename
#     table = Table(name, metadata,
#                   Column('timestamp', Integer, primary_key=True),
#                   Column('Channel 1', Float, nullable=False),
#                   Column('Channel 2', Float, nullable=False),
#                   Column('Channel 3', Float, nullable=False),
#                   Column('Channel 4', Float, nullable=False))
#     metadata.create_all(engine)
#     return name


# Add csv data to specified table
def send_data_from_csv(db: Session, tablename: str, csv_path: str):
    print("Sending data...")
    df = pd.read_csv(csv_path)
    send_data_from_df(db, tablename, df)


def send_data_from_df(db: Session, tablename: str, df: pd.DataFrame):
    conn = db.connection()
    df.to_sql(tablename, con=conn, if_exists='replace', index=False)
    try:
        db.commit()
        return True
    except IntegrityError as e:
        # raise ArithmeticError("Duplicate record exists")
        return False
