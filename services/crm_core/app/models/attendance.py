from app.models.base import BaseModelTenant

from tortoise import fields


class Attendance(BaseModelTenant):
    was_present = fields.BooleanField(default=False)

    lesson = fields.ForeignKeyField(
        "models.Lessons",
        related_name="attendances"
    )
    student = fields.ForeignKeyField(
        "models.Student",
        related_name="attendances"
    )

    comment = fields.TextField(null=True)

    class Meta:
        table = 'attendances'
    


    
