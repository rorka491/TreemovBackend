from app.models.base import BaseModelPK

from tortoise import fields


class Role(BaseModelPK):
    code = fields.CharField(max_length=50, unique=True)
    title = fields.CharField(max_length=100)

    class Meta:
        table = "roles"