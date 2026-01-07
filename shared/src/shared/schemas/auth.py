from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from shared.enums.auth import UserRole


class UserCreate(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    password: str = Field(min_length=6)


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: Optional[str] = None
    role: UserRole = UserRole.USER


class UserLogin(BaseModel):
    username: str 
    password: str


class UserList(BaseModel):
    users: list[UserRead]
