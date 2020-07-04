from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app import database
import datetime

# SAL Alchemy Models
class Patient(database):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    sex = Column(String)
    date = Column(datetime)

    items = relationship("Item", back_populates="owner")

class Item(database):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Patient", back_populates="items")