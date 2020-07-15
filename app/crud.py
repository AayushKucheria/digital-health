'''
CRUD = Create Read Update Delete
Add necessary sql functions here to use throughout the project.
'''

from sqlalchemy import MetaData, Table, Column, Integer, Float, String
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, inspector
from psycopg2 import sql
import pandas as pd
from sqlalchemy.exc import IntegrityError
# from psycopg2.


from fastapi.responses import FileResponse


# TODO Add security check fastapi

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


# # Add csv data to specified table
# def send_data(db: Session, tablename: str, csv_path: str):
#     # conn = engine.connect().connection
#     # cursor = conn.cursor()
#     # cursor.copy_from(data, tablename, columns=columns, sep=',', null='null')
#     # cursor.commit()
#     # # db.execute("INSERT INTO " + tablename + " VALUES (%s %s %s %s)", ())
#     # db.execute("COPY {} FROM '{}' DELIMITER ',' CSV;".format(tablename, csv_path))
#     # db.execute(("\COPY {} FROM '{}' (DELIMITER(','));".format(tablename, csv_path)))
#
#     copy_sql = "COPY {} FROM '{}' DELIMITER ',' CSV;".format(tablename, csv_path)
#     openfile = open(csv_path, 'r')
#     print(openfile)
#     # temp_conn = engine.raw_connection()
#     temp_curr = db.connection().connection.cursor() # temp_conn.cursor()
#     temp_curr.copy_from(openfile, tablename, sep=',', null='')
#     # temp_curr.copy_expert(copy_sql, openfile)
#     db.commit()

# # Add csv data to specified table
# def send_data(db: Session, tablename: str, data: list):
#     print("Send data function running")
#     print(data)
#     for i in data:
#         print(i)
#         temp_curr = db.connection().connection.cursor()
#         temp_curr.execute(
#             sql.SQL("insert into {} values (%s, %s, %s, %s)")
#             .format(sql.Identifier(tablename), float(i[0]), float(i[1]), float(i[2]), float(i[3])))
#         print("Added one row")
#     db.commit()

def send_data(db: Session, tablename: str, csv_path: str):
    df = pd.read_csv(csv_path)
    conn = db.connection()
    df.to_sql(tablename, con=conn, if_exists='replace', index=False)
    try:
        db.commit()
    except IntegrityError as e:
        raise ArithmeticError("Duplicate record exists")

