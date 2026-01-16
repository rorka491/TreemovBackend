from typing import TYPE_CHECKING
from tortoise.expressions import Q
from src.repo import UserRepository
from src.exceptions.user import UserAlreadyExistsException, UserNotFoundNotAuthException
from src.models.user import User
from src.core.config import hasher
from src.produce.producers import producer


from shared.enums.queue import QueueEnum
from shared.enums.profile import ProfileRole
from shared.schemas.user import UserRead, UserCreate
from shared.schemas.profile import ProfileCreate
from shared.payload import UserCreatedPayload, EmailVerifiedPayload
from shared.exceptions.user import UserNotFoundNotAuthException



class UserService: 
    def __init__(self):
        self.hasher = hasher
        self.repo = UserRepository()
        self.producer = producer

    async def get_all(self) -> list[User]:
        return await self.repo.get_all()

    async def _create_or_update_user(self, data: UserCreate) -> tuple[User, bool]:
        """
        Метод создаст пользователя или обновит неактивного или 
        выбросит исключение что такой пользователь есть
        """
        user = await self._update_exists_not_active_user(data)
        if user:
            return user, False

        return await self.repo.create(**data.model_dump()), True
    
    async def _update_exists_not_active_user(self, data: UserCreate) -> User | None:
        """
        Метод найдет пользователя и если он не активен тогда он будет обновлен
        По задумке нужно для того чтобы когда пользователь регистрировался 
        на его почту заняли но не активировали он мог вставить свои данные таким образом зарегистрироваться
        """
        user = await self.repo.get_user_by_email(email=data.email)

        if not user:
            return None

        if user.is_active:
            raise UserAlreadyExistsException

        return await self.repo.update(
            user,
            **data.model_dump(exclude_unset=True)
        )

    
    def _create_payload(self, user: User, role: str):
        """
        Метод валидирует выбранную роль таким образом чтобы она существовала в перечислении
        """
        role = ProfileRole(role)
        return UserCreatedPayload(user_id=user.id, role=role.value)

    async def handle_user_create(self, user_data: UserCreate, role: str):
        user, created = await self._create_or_update_user(user_data)
        
        if created:
            payload = self._create_payload(user=user, role=role)
            await self.producer.publish(payload=payload, queue=QueueEnum.USER_CREATED)

        return user
    
    async def activate_user(self, email: str):
        user = await self.repo.get_user_by_email(email=email)
        if not user:
            raise UserNotFoundNotAuthException

        user = await self.repo.update(obj=user, is_active=True)
        await user.save()
        return user

    async def get_user_by_username(self, username: str) -> User:
        user = await self.repo.get_user_by_username(username)
        if not user:
            raise UserNotFoundNotAuthException
        return user
    

    async def get_user_by_id(self, id: int) -> User:
        user = await self.repo.get(id=id)
        if not user:
            raise UserNotFoundNotAuthException
        return user
    



