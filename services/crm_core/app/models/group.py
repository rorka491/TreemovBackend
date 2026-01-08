from app.models.base import BaseModelTenant
from tortoise import fields
from typing import TYPE_CHECKING



class Group(BaseModelTenant):
    group_number = fields.CharField(max_length=20)
    type = fields.CharField(max_length=100)
    student_count = fields.IntField(default=0)

    class Meta:
        table = 'groups'
