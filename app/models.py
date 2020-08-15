from sqlalchemy import Column, Integer, String

import database


# SQL Alchemy Models
class Patient(database.Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(String)
    sex = Column(String)


class Result(database.Base):
    __tablename__ = "results"

    session_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    model_id = Column(Integer)
    result = Column(Integer)
    confidence = Column(Integer)
