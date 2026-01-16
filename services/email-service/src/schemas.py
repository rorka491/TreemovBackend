from pydantic import BaseModel, EmailStr, Field
from src.enums import CodePurpose, EventType
from datetime import datetime, UTC


class SendCodeSchema(BaseModel):
    email: EmailStr
    purpose: CodePurpose

class VerifyCodeSchema(BaseModel):
    email: EmailStr
    code: str
    purpose: CodePurpose

class CodeOutSchema(BaseModel):
    email: EmailStr
    code: str
    purpose: CodePurpose
    expires_at: datetime


class DomainEvent(BaseModel):
    event: EventType
    payload: dict
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


