from jose import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from src.enums import UserRole
from src.models.user import User
from src.services.user import UserService
from src.services.auth import AuthService
from src.core.config import PRIVATE_KEY, ALGORITHM, PUBLIC_KEY

from libs.auth import TokenService
from shared.exceptions import AdminsOnlyException, InvalidTokenException

def get_user_service():
    return UserService()

def get_auth_service():
    return AuthService()

def get_token_service():
    return TokenService(public_key=PUBLIC_KEY, alghoritms=[ALGORITHM])

auth_scheme = HTTPBearer()


async def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
    token_service: TokenService = Depends(get_token_service)
) -> int:
    token = credentials.credentials
    payload = token_service.verify_access_token(token)
    user_id = payload.get("sub")
    
    if not user_id:
        raise InvalidTokenException

    return user_id


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
    user_service: UserService = Depends(get_user_service)
) -> User:
    user_id = await get_current_user_id(credentials=credentials)
    user = await user_service.get_user_by_id(id=user_id)
    return user


async def get_current_admin(user=Depends(get_current_user)):
    if not user.role == UserRole.ADMIN:
        raise AdminsOnlyException
    return user
