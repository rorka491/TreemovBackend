from app.models.base import BaseModelTenant
from tortoise import fields


class Invite(BaseModelTenant):
    status = fields.CharField(max_length=50)
    role = fields.ForeignKeyField('models.Role', on_delete=fields.CASCADE)
    email = fields.CharField(max_length=255)
    profile = fields.ForeignKeyField(
        "models.Profile",
        related_name="invites"
    )

    class Meta:
        table = "invites"


