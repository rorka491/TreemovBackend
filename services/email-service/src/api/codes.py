from fastapi import APIRouter, status
from pydantic import BaseModel
from src.schemas import SendEmailSchema, SendRawEmailSchema

router = APIRouter(prefix="/codes", tags=["codes"])


@router.post(
    "/send",
    status_code=status.HTTP_202_ACCEPTED,
)
async def send_code(payload: SendCodeSchema):
    """
    Генерация + сохранение + отправка кода
    """
    return {"expires_in": payload.ttl}


@router.post(
    "/verify",
)
async def verify_code(payload: VerifyCodeSchema):
    """
    Проверка кода
    """
    return {"valid": True}
