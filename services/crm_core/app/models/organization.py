from tortoise import fields
from app.models.base import BaseModelPK, BaseModelTenant


class Organization(BaseModelPK):
    title = fields.CharField(max_length=255, unique=True)
