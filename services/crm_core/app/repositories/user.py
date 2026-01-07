from app.models.base import BaseModelPK
from app.models.user import User
from app.repositories.base import TenantRepository, TortoiseRepository
from tortoise.expressions import Q


class UserRepository(TortoiseRepository):
    model: type[BaseModelPK] = User

    async def create_user(self, **user_data):
        return await super().add(**user_data)

    async def get_user_by_login(self, login: str):
        return await self.get_by(login=login)

    async def get_user_by_email(self, email: str):
        return await self.get_by(email=email)

    async def user_exists(self, email: str, login: str):
        return await self.model.filter(Q(email=email) | Q(login=login)).exists()
