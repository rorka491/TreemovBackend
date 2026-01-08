from app.models.base import BaseModelTenant
from tortoise import fields


class Invite(BaseModelTenant):
    status = fields.CharField(max_lenght=50)
    email = fields.CharField(max_lenght=100)

    student_profile = fields.ForeignKeyField(
        "models.Profile",
        related_name="invites"
    )

    class Meta:
        table = "invites"

# class InviteTeacher(BaseModelTenant):
#     status = fields.CharField(max_lenght=50)
#     email = fields.CharField(max_lenght=100)

#     student_profile = fields.ForeignKeyField(
#         "models.Profile",
#         related_name="teacher_invites"
#     )

#     class Meta:
#         table = "teacher_invites"