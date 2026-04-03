from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

VALID_TYPES = ["income", "expense"]


# USER SCHEMAS
class UserCreate(BaseModel):
    name: str
    email: str
    role: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True


# TRANSACTION CREATE
class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: str

    @field_validator("amount")
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Amount must be positive")
        return v

    @field_validator("type")
    def type_must_be_valid(cls, v):
        if v.lower() not in VALID_TYPES:
            raise ValueError("Type must be 'income' or 'expense'")
        return v.lower()


# TRANSACTION UPDATE
class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    type: Optional[str] = None
    category: Optional[str] = None
    date: Optional[date] = None
    notes: Optional[str] = None

    @field_validator("amount")
    def validate_amount(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Amount must be positive")
        return v

    @field_validator("type")
    def validate_type(cls, v):
        if v is not None and v.lower() not in VALID_TYPES:
            raise ValueError("Invalid type")
        return v.lower() if v else v


# RESPONSE
class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date
    notes: str
    user_id: int

    class Config:
        from_attributes = True