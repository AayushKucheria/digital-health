from sqlalchemy import Column, Integer, String

import database


# SQL Alchemy Models
class Patient(database.Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(String)
    sex = Column(String)
