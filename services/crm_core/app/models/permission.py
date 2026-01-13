from app.models.base import BaseModelPK
from tortoise import fields, models


class Permission(BaseModelPK):
    code = fields.CharField(max_length=100, unique=True)
    name = fields.CharField(max_length=255)

    class Meta:
        table = "permissions"


class RolePermission(BaseModelPK):
    permission = fields.ForeignKeyField(
        "models.Permission",
        related_name="role_permissions"
    )
    role = fields.ForeignKeyField(
        "models.Role",
        related_name="role_permissions"
    )

    class Meta:
        table = 'role_permissions'
        unique_together = ('role', 'permission')