from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobApplicationBase(BaseModel):
    company: str
    position: str
    status: str
    applied_date: datetime
    notes: Optional[str] = None

class JobApplicationCreate(JobApplicationBase):
    pass

class JobApplication(JobApplicationBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: str
    password: str

class User(UserCreate):
    id: int

    class Config:
        orm_mode = True
