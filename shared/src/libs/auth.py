from typing import Optional
from shared.exceptions.auth import InvalidTokenException, InvalidUserCredentials, PublicKeyNotProvided, UserIsNotActive
from jose import jwt, JWTError



class TokenService:
    def __init__(self, alghoritms: list, public_key: str = None):
        self.alghoritms = alghoritms
        self.public_key = public_key

    def _verify_token(self, token: str) -> dict:
        if not self.public_key:
            raise PublicKeyNotProvided
        try:
            payload = jwt.decode(
                token, self.public_key, algorithms=self.alghoritms # pyright: ignore[reportArgumentType]
            )
        except JWTError:
            raise InvalidTokenException
        if payload.get("is_active") is False:
            raise UserIsNotActive
        return payload

    def verify_access_token(self, token: str)  -> Optional[dict]:
        payload = self._verify_token(token)
        if payload.get("type") != "access":
            raise InvalidTokenException
        return payload

    def verify_refresh_token(self, token: str) -> Optional[dict]:
        payload = self._verify_token(token)
        if payload.get("type") != "refresh":
            raise InvalidTokenException
        return payload