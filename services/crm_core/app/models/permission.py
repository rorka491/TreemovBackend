from app.models.base import BaseModelPK
from tortoise import fields


class Permission(BaseModelPK):
    code = fields.CharField(max_length=100, unique=True)
    name = fields.CharField(max_length=255)

    class Meta:
        table = "permissions"


class RolePermission(BaseModelPK):
    permission = fields.ForeignKeyField(
        "models.Permission",
        related_name="permissions"
    )
    role = fields.ForeignKeyField(
        "models.Role"
    )

    class Meta:
        unique_together = ('role', 'permission')
