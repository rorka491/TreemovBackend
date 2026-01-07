from abc import ABC, abstractmethod
from app.models.base import BaseModelPK

class AbstractRepository(ABC):

    @abstractmethod
    async def add():
        raise NotImplementedError
                      
    @abstractmethod    
    async def get_all():
        raise NotImplementedError
    
    @abstractmethod    
    async def get_by():
        raise NotImplementedError


class TortoiseRepository(AbstractRepository):
    model: BaseModelPK = None


    async def add(self, **kwargs):
        return await self.model.create(**kwargs)
    
    async def get_by(self, **filter_by):
        return await self.model.get_or_none(**filter_by)

    async def get_all(self, **filter_by):
        qs = self.model.filter(**filter_by) if filter_by else self.model.all()
        return await qs


class TenantRepository(TortoiseRepository):
    org: str | int = None

    def __init__(self, org):
        self.org_ = org

    async def add(self, **kwargs):
        kwargs["org_id"] = self.org
        return await self.model.create(**kwargs)

    async def get_by(self, **filter_by):
        filter_by["org_id"] = self.org
        return await super().get_by(**filter_by)

    async def get_all(self, **filter_by):
        filter_by["org_id"] = self.org
        return await super().get_all(**filter_by)
