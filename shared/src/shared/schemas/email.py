from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, UTC
from shared.enums.email import EmailCodePurpose



class SendCodeSchema(BaseModel):
    email: EmailStr
    purpose: EmailCodePurpose

class VerifyCodeSchema(BaseModel):
    email: EmailStr
    code: str
    purpose: EmailCodePurpose


class CodeOutSchema(BaseModel):
    email: EmailStr
    code: str
    purpose: EmailCodePurpose
    expires_at: datetime


class EmailEvent(BaseModel):
    payload: VerifyCodeSchema
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    class Config:
        json_encoders = {
            datetime: lambda v: v.replace(microsecond=0).isoformat()
        }
