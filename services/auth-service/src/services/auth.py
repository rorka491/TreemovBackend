from src.repo import UserRepository
from src.services.token import create_access_token, create_refresh_token, verify_access_token, verify_refresh_token, is_blacklisted, blacklist_token
from shared.schemas.user import UserLogin
from src.models.user import User
from src.core.logger import logger
from src.core.config import hasher, redis_client, argon2, ALGORITHM, PUBLIC_KEY
from shared.exceptions.auth import InvalidUserCredentials, InvalidTokenException, TokenBlackListedException, JtiNotProvided
from libs.auth import TokenService

class AuthService:
    def __init__(self):
        self.hasher: argon2 = hasher
        self.repo = UserRepository()
        self.token_service = TokenService(public_key=PUBLIC_KEY, alghoritms=[ALGORITHM])

    async def authenticate_user(self, data: UserLogin) -> tuple[str, str]:
        user = await self.repo.get_user_by_email(email=data.email)
        if not user or not user.is_active:
            raise InvalidUserCredentials

        if not self.hasher.verify(data.password, user.password):
            raise InvalidUserCredentials

        access_token = create_access_token(user)
        refresh_token = create_refresh_token(user)
        

        return access_token, refresh_token

    async def get_new_access_token(self, refresh_token: str) -> str | None :
        payload = self.token_service.verify_refresh_token(refresh_token)
        await self.get_jti_or_exception(payload)
        user = await self.get_user_or_exception(payload)
        access_token = create_access_token(user)
        return access_token 

    async def get_user_data(self, access_token: str) -> User: 
        payload = self.token_service.verify_refresh_token(access_token)
        return await self.get_user_or_exception(payload)

    async def get_user_or_exception(self, payload: dict) -> User:
        user_id = payload.get('sub')
        user = await self.repo.get(id=user_id)
        if not user:
            raise InvalidUserCredentials
        return user

    async def get_jti_or_exception(self, payload: dict) -> str:
        jti = payload.get('jti')
        if not jti:
            raise JtiNotProvided

        if await is_blacklisted(jti):
            raise TokenBlackListedException
        return jti

    async def logout(self, refresh_token: str):
        try:
            payload = verify_refresh_token(refresh_token)
        except Exception:
            raise InvalidTokenException

        jti = payload.get("jti")
        exp = payload.get("exp")

        if not jti or not exp:
            raise InvalidTokenException

        await blacklist_token(jti, exp)
