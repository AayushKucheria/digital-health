# Pydantic Models (Schemas)

from pydantic import BaseModel


# TODO: What if I keep just 1 class for patient and result each?

# base Class
from sqlalchemy import UniqueConstraint


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

    # To allow creation from arbitrary class instances?
    class Config:
        orm_mode = True


class ResultBase(BaseModel):

    __table_args__ = (
        UniqueConstraint("patient_id", "model_id", "session_id")
    )
    patient_id: int
    model_id: int
    result: int
    # confidence: int



class ResultCreate(ResultBase):
    __table_args__ = (
        UniqueConstraint("patient_id", "model_id", "session_id")
    )
    session_id: int


class Result(ResultBase):
    __table_args__ = (
        UniqueConstraint("patient_id", "model_id", "session_id")
    )
    session_id: int

    class Config:
        orm_mode = True
