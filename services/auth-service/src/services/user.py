from typing import TYPE_CHECKING
from tortoise.expressions import Q
from src.repo import UserRepository
from src.exceptions.user import UserAlreadyExistsException, UserNotFoundNotAuthException
from src.models.user import User
from src.core.config import hasher
from src.produce.producers import producer


from shared.enums.queue import QueueEnum
from shared.schemas.user import UserRead, UserCreate
from shared.schemas.profile import ProfileCreate
from shared.payload import UserCreatedPayload



class UserService: 
    def __init__(self):
        self.hasher = hasher
        self.repo = UserRepository()
        self.producer = producer

    async def get_all(self) -> list[User]:
        return await self.repo.get_all()

    async def _create_user(self, data: UserCreate) -> User:
        user = await self._update_exists_not_active_user(data)
        if user:
            return user

        return await self.repo.create(data)
    
    async def _update_exists_not_active_user(self, data: UserCreate) -> User | None:
        user = await self.repo.get_user_by_email(email=data.email)

        if not user:
            return None

        if user.is_active:
            raise UserAlreadyExistsException

        return await self.repo.update(
            user_id=user.id,
            **data.model_dump(exclude_unset=True)
        )

    async def handle_user_create(self, profile_data: ProfileCreate, user_data: UserCreate):
        user = await self._create_user(user_data)

        payload = UserCreatedPayload(
            user_id=user.id,
            **profile_data.model_dump()
        )
        await self.producer.publish(payload=payload, queue=QueueEnum.USER_CREATED)
        return user
    
    
    async def get_user_by_username(self, username) -> User:
        user = await self.repo.get_user_by_username(username)
        if not user:
            raise UserNotFoundNotAuthException
        return user
    

    async def get_user_by_id(self, id: int) -> User:
        user = await self.repo.get(id=id)
        if not user:
            raise UserNotFoundNotAuthException
        return user


