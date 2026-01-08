from tortoise import models, fields
from app.models.base import BaseModelPK, BaseModelTenant
from app.constants import UserRole


class AstractUser(BaseModelPK):
    login = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)

    class Meta:
        abstract = True        


class User(AstractUser):
    email = fields.CharField(max_length=255, unique=True)
    role = fields.CharEnumField(enum_type=UserRole)
