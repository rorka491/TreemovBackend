from app.models.base import BaseModelTenant
from tortoise import fields
from typing import TYPE_CHECKING



class StudentGroup(BaseModelTenant):
    title = fields.CharField(max_length=255)

    class Meta:
        table = 'student_group'
