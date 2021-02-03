from typing import List, Optional

from pydantic import BaseModel

from app.models import Species


class BearBase(BaseModel):
    name: str
    species: Species


class Bear(BearBase):
    id: int
    owner: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    bears: List[Bear] = []

    class Config:
        orm_mode = True
