from typing import Optional 
from pydantic import BaseModel, Field, EmailStr
from shared.enums.auth import UserRole
from shared.enums.profile import ProfileRole




class UserCreatedPayload(BaseModel):
    user_id: int
    role: str

class UserActivatePayload(BaseModel):
    user_id: int

class EmailVerifiedPayload(BaseModel):
    email: EmailStr
    purpose: str

