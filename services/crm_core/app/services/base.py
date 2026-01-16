from pydantic import BaseModel
from app.repositories.tortoise import TortoiseRepository, TenantRepository
from app.filters import BaseModelFilter
from tortoise.exceptions import IntegrityError
from shared.exceptions import UniqueFieldRequiredException, ObjectNotFound



class BaseService:
    repo_cls: type[TortoiseRepository] = None

    def __init__(self):
        self.repo = self.repo_cls()

    async def create(self, obj_schema: BaseModel):
        try:
            obj = await self.repo.create(**obj_schema.model_dump())
        except IntegrityError:
            raise UniqueFieldRequiredException
        
        prefecthed_obj = await self.repo.prefetch_obj(obj)
        return prefecthed_obj


    async def update(self, id: int , obj_schema: BaseModel):
        obj = await self.get_by_id(id=id)
        try:
            obj = await self.repo.update(obj, **obj_schema.model_dump(exclude_unset=True))
        except Exception as e:
            raise e
        prefecthed_obj = await self.repo.prefetch_obj(obj)
        return prefecthed_obj
    
    
    async def get_by_id(self, id: int):
        obj = await self.get(id=id)
        prefecthed_obj = await self.repo.prefetch_obj(obj)
        return prefecthed_obj
    

    async def get(self, **filters):
        obj = await self.repo.get(**filters)
        if not obj:
            raise ObjectNotFound
        return obj
    
    
    async def get_all(self, query_filters: BaseModelFilter = None) -> list:
        filters = {}
        if query_filters: 
            filters = await query_filters.to_tortoise_filters()

        query = await self.repo.get_all(**filters)
        queryset = await self.repo.prefetch_queryset(query)
        return await queryset.all() 


    async def delete(self, id: int):
        obj = await self.get(id=id)
        return await self.repo.delete(obj=obj)
    

class BaseServiceTenant(BaseService):
    repo_cls: type[TenantRepository] = None

    def __init__(self, org):
        self.repo = self.repo_cls(org)

