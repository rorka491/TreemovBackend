from pydantic import BaseModel, Field, EmailStr
from shared.enums.auth import UserRole



class UserCreatedPayload(BaseModel):
    user_id: int
    email: EmailStr
    role: UserRole = UserRole.USER


class EmailVerifiedPayload(BaseModel):
    user_id: int
    email: EmailStr
