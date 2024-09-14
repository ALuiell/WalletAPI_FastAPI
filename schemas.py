from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, timezone


class Category(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., max_length=255)

    class Config:
        orm_mode = True


class UserAccount(BaseModel):
    id: Optional[int] = None
    number: str = Field(..., max_length=8)
    type: str
    name: str
    balance: float = 0.0

    class Config:
        orm_mode = True


class Transaction(BaseModel):
    id: Optional[int] = None
    number_id: UserAccount = Field(...)
    type: str
    category_id: Category = Field(...)
    date: Optional[datetime] = None
    transaction_id: Optional[UUID] = None
    amount: float

    class Config:
        orm_mode = True

