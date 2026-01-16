from abc import ABC, abstractmethod
from tortoise.models import Model
from tortoise.expressions import Q
from typing import Type, Optional, List, TypeVar
from src.models.user import User
from src.core.config import hasher


M = TypeVar('M', bound=Model)

class AbstractRepository(ABC):
    model: Type[M]

    @abstractmethod
    async def get(self, **filters) -> Optional[M]:
        ...

    @abstractmethod
    async def get_all(self) -> List[M]:
        ...

    @abstractmethod
    async def filter(self, **filters) -> List[M]:
        ...

    @abstractmethod
    async def create(self, **data) -> M:
        ...

    @abstractmethod
    async def update(self, obj: M, **data) -> M:
        ...


class TortoiseRepository(AbstractRepository):
    
    async def get_all(self) :
        return await self.model.all()
    
    async def get(self, **filters):
        return await self.model.get_or_none(**filters)
    
    async def create(self, **data):
        return await self.model.create(**data)
    
    async def update(self, obj: M, **data):
        obj = await obj.update_from_dict(data)
        obj.save()
        return obj

    async def filter(self, **filters):
        return await self.model.filter(**filters)


class UserRepository(TortoiseRepository):
    model = User

    async def create(self, **data):
        password = data.get("password")
        data['password'] = hasher.hash(password)
        return await super().create(**data)
    
    async def update(self, obj, **data):
        password = data.pop("password", None)

        if password is not None:
            data["password"] = hasher.hash(password)

        return await super().update(obj, **data)

    async def update_password(self, password: str):
        return await self.update(password=password)

    async def active_user_exists(self, email: str) -> bool:
        return await self.model.filter(Q(email=email) & Q(is_active=True)).exists()
    
    async def get_user_by_username(self, username: str) -> User | None:
        return await self.model.get_or_none(username=username)
     
    async def get_user_by_email(self, email: str) -> User | None:
        return await self.model.get_or_none(email=email)
