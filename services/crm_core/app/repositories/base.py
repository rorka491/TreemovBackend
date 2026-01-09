from typing import TypeVar, Optional, List, Type
from tortoise import Model
from tortoise.queryset import QuerySet, QuerySetSingle
from abc import ABC, abstractmethod
from app.models.base import BaseModelPK
from app.decorators import handle_relations

M = TypeVar('M', bound=Model)


class AbstractRepository(ABC):
    model: Type[M]

    @abstractmethod
    async def get(self, **filters) -> Optional[M]:
        ...

    @abstractmethod
    def get_all(self) -> List[M]:
        ...

    @abstractmethod
    async def filter(self, **filters) -> List[M]:
        ...

    @abstractmethod
    async def create(self, **data) -> M:
        ...

    @abstractmethod
    async def extract_relation_fields(self, **data) -> dict[str: int]:
        ...

    @abstractmethod
    async def update(self, obj: M, **data) -> M:
        ...

