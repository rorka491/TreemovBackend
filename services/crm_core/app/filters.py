from datetime import timedelta
from typing import Optional, Sequence
from pydantic import BaseModel


class BaseModelFilter(BaseModel):
    async def to_tortoise_filters(self):
        filters = {}
        
        for field_name, field_value in self.model_dump(exclude_none=True).items():
            if field_name.endswith('_min'):
                base = field_name.removesuffix('_min')
                filters[f"{base}__gte"] = field_value
                continue
            elif field_name.endswith('_max'):
                base = field_name.removesuffix('_max')
                filters[f"{base}__lte"] = field_value
                continue
            elif isinstance(field_value, (list, tuple, set)):
                if field_value: 
                    filters[f"{field_name}__in"] = field_value
        return filters
    

