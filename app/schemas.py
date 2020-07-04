# Pydantic Models (Schemas)

from typing import List, Optional
from pydantic import BaseModel


# Base class for item. All common attributes
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


# Inherited class with extra attributes
class ItemCreate(ItemBase):
    pass


# Schemas for reading data
# We know an item has an id if it's been defined
class Item(ItemBase):
    id: int
    patient_id: int

    # Tells Pydantic model to read data even if
    # it's not dict but an ORM model or any other
    # object with attributes
    class Config:
        orm_mode = True


# base Class
class PatientBase(BaseModel):
    sex: str
    age: int


# Inherited class with extra attributes while creation
class PatientCreate(PatientBase):
    # age: int
    id: int
    # sex: str
    # ohgod: str


# Schema for reading
class Patient(PatientBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
