from tortoise import fields
from tortoise.backends.base.client import BaseDBAsyncClient
from typing import Any
from datetime import timedelta


class TimeDurationField(fields.IntField):

    python_type = timedelta

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_db_value(self, value: Any, instance) -> Any:
        if value is None:
            return None
        return int(value.total_seconds())

    def to_python_value(self, value: Any) -> Any:
        if value is None:
            return None
        if isinstance(value, timedelta):
            return value 
        return timedelta(seconds=value)

