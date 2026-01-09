from typing import Any
from app.models.base import BaseModelPK, BaseModelTenant
from tortoise import fields


class Student(BaseModelTenant):
    name = fields.CharField(max_length=100)
    surname = fields.CharField(max_length=100)
    progress = fields.DecimalField(max_digits=5, decimal_places=2, default=0)
    birthday = fields.DateField()
    score = fields.IntField(default=0)
    class Meta: 
        table = 'students'

    def __str__(self):
        return self.name


class StudentGroupMember(BaseModelTenant):
    student = fields.ForeignKeyField(
        "models.Student",
        related_name="group_memberships"
    )
    group = fields.ForeignKeyField(
        "models.Group",
        related_name="members" 
    )

    class Meta:
        table = 'student_group_members'

