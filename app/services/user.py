from typing import TypeVar, Generic
from fastapi.exceptions import HTTPException
from app.schemas.user import UserCreate
from app.core.config import pwd_context
from app.repositories.user import UserRepository
from app.core.config import logger


class AbstractService:

    def __init__(self, repo) -> None:
        self.repo = repo


class UserService(AbstractService):

    async def create_user(self, user_data: UserCreate):
        user_exists = await self.repo.user_exists(
            email=user_data.email,
            login=user_data.login            
        )
        if user_exists:
            raise HTTPException(400, 'User with this login or email already exists')

        data = user_data.model_dump()
        password = data.get('password')
        hash_pass = pwd_context.hash(password)
        data['password'] = hash_pass
        user = self.repo.create_user(**data)
        return await user
