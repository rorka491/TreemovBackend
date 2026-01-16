from tortoise import fields
from src.models.base import BaseModelPK
from datetime import datetime, UTC
from src.enums import CodePurpose, DeliveryChannel


class EmailCode(BaseModelPK):
    email = fields.CharField(max_length=255)
    code = fields.CharField(max_length=6)
    purpose = fields.CharEnumField(CodePurpose, max_length=50)
    is_used = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    expires_at = fields.DatetimeField()
    
    @property
    def is_expired(self) -> bool:
        return self.expires_at < datetime.now(UTC)

    @property
    def is_used(self) -> bool:
        return self.used_at is not None