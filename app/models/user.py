# app/models/user.py
from pydantic import BaseModel
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    password = Column(String)
    gender = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    gender: str

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    gender: str
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    name: str
    gender: str