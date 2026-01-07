from fastapi import APIRouter, Request, Depends
from app.schemas.credentials import UserCredentialsModel
from app.services.auth import AuthService
from app.depends.auth import get_auth_service

router = APIRouter(prefix='/token')


@router.post('')
async def auth_token(
    credentials: UserCredentialsModel,
    auth_service: AuthService = Depends(get_auth_service),
):
    access_token = await auth_service.check_credentials(credentials)
    return {"access_token": access_token}
