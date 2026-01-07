from datetime import datetime, timezone, timedelta
from jose import jwt
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.credentials import UserCredentialsModel
from app.repositories.user import UserRepository
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, pwd_context

class AuthService:

    def __init__(self, user_repo: UserRepository):
        self.user_repo: UserRepository = user_repo

    async def check_credentials(self, credentials: UserCredentialsModel) -> str:
        user: User = await self.user_repo.get_user_by_login(credentials.login)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid login or password",
            )

        if not pwd_context.verify(credentials.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid login or password",
            )

        return self._create_access_token({"sub": str(user.id)})

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Проверяет пароль"""
        return pwd_context.verify(plain_password, hashed_password)
    
    def _create_access_token(self, user_id: int) -> str:
        """
        Создает JWT access token
        """
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.now(timezone.utc) + expires_delta
        
        to_encode = {
            "sub": str(user_id),
            "exp": expire,
            "type": "access"
        }
        
        try:
            return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        except JWTError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not create access token"
            )

    def _create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})

        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
