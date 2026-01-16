from app.models.base import BaseModelTenant

from tortoise import fields
from enum import Enum



class AccuralCategory(Enum):
    ATTENDANCE = "attendance"
    PARTICIPATION = "participation"
    BEHAVIOR = "behavior"
    ACHIEVEMENTS = "achievements"
    HOMEWORK = "homework"


class Accrual(BaseModelTenant):
    amount = fields.IntField(default=0)
    comment = fields.CharField(max_length=255)

    teacher = fields.ForeignKeyField(
        "models.Profile",
        related_name="accruals"  
    )

    student = fields.ForeignKeyField(
        "models.Student",
        related_name="accruals"  
    )
    category = fields.CharEnumField(
        AccuralCategory,
        default=AccuralCategory.ATTENDANCE
    )

    class Meta:
        table = "accruals"