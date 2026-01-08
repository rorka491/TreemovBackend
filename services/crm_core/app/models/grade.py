from app.models.base import BaseModelTenant
from tortoise import fields
from typing import TYPE_CHECKING


class Grade(BaseModelTenant):
    value = fields.IntField(default=0, null=True)
    comment = fields.TextField(null=True)
    grade_date = fields.DateField(null=True)

    lesson = fields.ForeignKeyField(
        "models.Lessons",
        related_name="grades"
    )
    student = fields.ForeignKeyField(
        "models.Student",
        related_name="grades"
    )

    class Meta:
        table = "grades"