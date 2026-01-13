from pydantic import BaseModel, Field, EmailStr
from shared.enums.auth import UserRole



class UserCreatedPayload(BaseModel):
    user_id: int
    name: str
    surname: str
    pathronamic: str 


class EmailVerifiedPayload(BaseModel):
    email: EmailStr
