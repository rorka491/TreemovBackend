from app.schemas.base import BaseModelCreate, BaseModelRead, BaseModelUpdate
from app.constants import UserRole                                          
from pydantic import EmailStr, field_validator, Field
from typing import Optional

class UserCreate(BaseModelCreate):
    login: str
    password: str
    repeat_password: str = Field(..., serialization_exclude=True)
    email: EmailStr
    role: Optional[UserRole] = UserRole.MANAGER

    @field_validator("repeat_password")
    def passwords_match(cls, v, info):
        password = info.data.get("password")
        if password != v:
            raise ValueError("Passwords do not match")
        return v


class UserUpdate(BaseModelUpdate): 
    login: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[UserRole] = None

class UserRead(BaseModelRead):
    login: str
    email: EmailStr
    role: UserRole
