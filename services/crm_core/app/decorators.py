from functools import wraps
from typing import Type, Optional, List, TypeVar, Callable
from tortoise.fields.relational import ManyToManyRelation, ForeignKeyRelation

def handle_relations(func: Callable):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        m2m_data, fk_data, clean_data = await self.extract_relation_fields(**kwargs)

        obj = await func(self, *args, **clean_data)

        await self.handle_fk_relations(obj, fk_data)

        for field, ids in m2m_data.items():
            if not ids:
                continue
            m2m_relation: ManyToManyRelation = getattr(obj, field)
            related_model = m2m_relation.remote_model
            related_objects = await related_model.filter(id__in=ids)
            await m2m_relation.add(*related_objects)
        await obj.save()
        return obj
    return wrapper


