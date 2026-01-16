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
        "models.Role",
        related_name="mebmer_role"
    )

    class Meta:
        table = 'organization_member'
