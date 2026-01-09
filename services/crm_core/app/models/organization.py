from tortoise import fields
from app.models.base import BaseModelPK, BaseModelTenant


class Organization(BaseModelPK):
    title = fields.CharField(max_length=255, unique=True)


class OrganizationMember(BaseModelTenant):
    user_profile = fields.ForeignKeyField(
        "models.Profile",
        null=True,
        related_name="organization_members"
    )
    role = fields.ForeignKeyField(
        "models.Roles",
        related_name="mebmer_role"
    )

# class OrganizationMember(BaseModelTenant):
#     student_organization_member = fields.ForeignKeyField(
#         "models.StudentProfile",
#         null=True,
#         related_name="student_organization_members"
#     )
#     teacher_organization_member = fields.ForeignKeyField(
#         "models.TecherProfile",
#         null=True,
#         related_name="techer_organization_members"
#     )
#     manager_organization_member = fields.ForeignKeyField(
#         "models.ManagerStudent",
#         null=True,
#         related_name="manager_organization_members"
#     )
