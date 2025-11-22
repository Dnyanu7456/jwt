# schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class NoteCreate(BaseModel):
    title: str
    content: Optional[str] = None

class NoteOut(BaseModel):
    id: int
    title: str
    content: Optional[str]
    owner_id: int
    created_at: datetime
    class Config:
        orm_mode = True
