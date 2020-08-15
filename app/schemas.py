# Pydantic Models (Schemas)

from pydantic import BaseModel


# TODO: What if I keep just 1 class for patient and result each?

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

    # To allow creation from arbitrary class instances?
    class Config:
        orm_mode = True


class ResultBase(BaseModel):
    patient_id: int
    model_id: int
    result: int
    confidence: int


class ResultCreate(PatientBase):
    session_id: int


class Result(ResultBase):
    session_id: int

    class Config:
        orm_mode = True
