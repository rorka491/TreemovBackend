from typing import Optional
from shared.exceptions.auth import InvalidTokenException, InvalidUserCredentials
from jose import jwt, JWTError


def verify_token(token: str, public_key: str, alghoritms: list) -> dict:
    try:
        payload = jwt.decode(
            token, public_key, algorithms=alghoritms # pyright: ignore[reportArgumentType]
        )
        return payload
    except JWTError:
        raise InvalidTokenException

def verify_access_token(token: str)  -> Optional[dict]:
    payload = verify_token(token)
    if payload.get("type") != "access":
        raise InvalidTokenException
    return payload

def verify_refresh_token(token: str) -> Optional[dict]:
    payload = verify_token(token)
    if payload.get("type") != "refresh":
        raise InvalidTokenException
    return payload