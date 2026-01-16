from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from src.schemas import SendCodeSchema, VerifyCodeSchema
from src.services.email import EmailService
from src.depends import get_email_service

router = APIRouter(prefix="/email", tags=["email"])


@router.post(
    "/send",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Send email using template",
)
async def send_email(
    payload: SendCodeSchema,
    email_service: EmailService = Depends(get_email_service)
):
    await email_service.send_code(payload)
    return {"message": "email queued"}


@router.post(
    "/verify",
    status_code=status.HTTP_202_ACCEPTED
)
async def verify_email(
    payload: VerifyCodeSchema,
    email_service: EmailService = Depends(get_email_service)
):
    is_verify = await email_service.verify_code(payload)
    if is_verify:
        ...
    ...

@router.get(
    "/health",
    summary="Email service healthcheck",
)
async def email_health():
    return {"status": "ok"}
