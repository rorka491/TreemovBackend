from app.models.base import BaseModelTenant

from tortoise import fields
from enum import Enum



class AccuralCategory(Enum):
    ATTENDANCE = "attendance", "Посещаемость"
    PARTICIPATION = "participation", "Участие"
    BEHAVIOR = "behavior", "Поведение"
    ACHIEVEMENTS = "achievements", "Достижения"
    HOMEWORK = "homework", "Домашнее задание"


class Accrual(BaseModelTenant):
    amount = fields.IntField(default=0)
    comment = fields.CharField(max_length=255)

    teacher = fields.ForeignKeyField(
        "models.Profile",
        related_name="transactions"  
    )

    student = fields.ForeignKeyField(
        "models.Student",
        related_name="transactions"  
    )
    category = fields.CharEnumField(
        AccuralCategory,
        default=AccuralCategory.ATTENDANCE
    )

    class Meta:
        table = "transactions"