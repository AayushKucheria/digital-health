from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import database
import datetime


# SQL Alchemy Models
class Patient(database.Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    sex = Column(String)
    # date = Column(datetime)

    items = relationship("Item", back_populates="owner")


class Item(database.Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))

    owner = relationship("Patient", back_populates="items")
