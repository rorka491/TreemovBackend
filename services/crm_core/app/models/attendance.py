from app.models.base import BaseModelTenant

from tortoise import fields


class Attendance(BaseModelTenant):
    was_present = fields.BooleanField(default=False)

    lesson = fields.ForeignKeyField(
        "models.Lesson",
    )
    student = fields.ForeignKeyField(
        "models.Student",
    )

    comment = fields.TextField(null=True)

    class Meta:
        table = 'attendances'





    
