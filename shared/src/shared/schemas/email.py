from pydantic import BaseModel, EmailStr, Field
from shared.enums.email import EmailCodePurpose
from datetime import datetime, UTC
from contracts.base import QueueEnum


class SendCodeSchema(BaseModel):
    email: EmailStr
    purpose: QueueEnum

class VerifyCodeSchema(BaseModel):
    email: EmailStr
    code: str
    purpose: QueueEnum

class CodeOutSchema(BaseModel):
    email: EmailStr
    code: str
    purpose: QueueEnum
    expires_at: datetime


class EmailEvent(BaseModel):
    event: QueueEnum
    payload: VerifyCodeSchema
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    class Config:
        json_encoders = {
            datetime: lambda v: v.replace(microsecond=0).isoformat()
        }
