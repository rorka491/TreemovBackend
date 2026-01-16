from tortoise import models, fields

class BaseModelPK(models.Model):
    id = fields.IntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelTenant(BaseModelPK):
    org = fields.ForeignKeyField('models.Organization', on_delete=fields.CASCADE)

    class Meta:
        abstract = True



