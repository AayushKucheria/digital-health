# Pydantic Models (Schemas)

from pydantic import BaseModel


# base Class
class PatientBase(BaseModel):
    sex: str
    age: int
    name: str


# Inherited class with extra attributes while creation
class PatientCreate(PatientBase):
    id: int


# Schema for reading
class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True
