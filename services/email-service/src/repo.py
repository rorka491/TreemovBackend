from functools import wraps
from typing import Type, Optional, List, TypeVar, Callable
from abc import ABC, abstractmethod
from tortoise.models import Model
from tortoise.fields.relational import ManyToManyRelation
from tortoise.queryset import QuerySet
from tortoise.expressions import Q
from tortoise.fields.relational import ManyToManyRelation, ForeignKeyRelation
from src.decorators import handle_relations
from src.models.code import VerificationCode


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


class TortoiseRepository(AbstractRepository):    
    def __init__(self):
        self.m2m_fields: list = self.get_m2m_fields()
        self.fk_fields: list  = self.get_fk_fields()

    def base_qs(self, **filters):
        return self.model.all().filter(**filters)
    

    async def prefetch_obj(self, obj: M) -> M:
        if self.m2m_fields:
            for field_name in self.m2m_fields:
                await obj.fetch_related(field_name)
        return obj
    

    async def prefecthed_list(self, objects: list[M]) -> list[M]:
        if self.m2m_fields:
            for obj in objects:
                await self.prefetch_obj(obj)
        return objects
    

    async def get_all(self, **filters):
        return await self.base_qs(**filters)
    
    
    async def paginate_get_all(
        self,
        *,
        limit: int = 20,
        offset: int = 0,
        **filters
    ) -> list[M]:
        return await (
            self.base_qs(**filters)
            .limit(limit)
            .offset(offset)
        )


    async def get(self, **filters):
        return await self.model.get_or_none(**filters)
    

    @handle_relations
    async def create(self, **data):
        return await self.model.create(**data)
    

    @handle_relations
    async def update(self, obj: M, **data):
        return await obj.update_from_dict(data)


    def get_m2m_fields(self) -> set:
        return self.model._meta.m2m_fields
    
    
    def get_fk_fields(self) -> set:
        return self.model._meta.fk_fields
    

    async def extract_relation_fields(self, **data) -> tuple[dict, dict, dict]:
        m2m_relation_data = {field: data.pop(field) for field in list(data.keys()) if field in self.m2m_fields}
        fk_relation_data = {field: data.pop(field) for field in list(data.keys()) if field in self.fk_fields}

        return m2m_relation_data, fk_relation_data, data
    

    async def delete(self, obj: M):
        return await obj.delete()
    
    
    async def handle_fk_relations(self, obj: M, fk_data: dict[str, int]):
        if not fk_data:
            return
        for field, value in fk_data.items():
            if value is not None:
                setattr(obj, f"{field}_id", value)
        await obj.save()

class VerificationCodeRepository(TortoiseRepository):
    model = VerificationCode()

