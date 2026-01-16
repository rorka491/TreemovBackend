from tortoise import fields
from src.models.base import BaseModelPK
from datetime import datetime, UTC
from src.enums import CodePurpose, DeliveryChannel

class VerificationCode(BaseModelPK):
    destination = fields.CharField(max_length=255)  

    channel = fields.CharEnumField(
        enum_type=DeliveryChannel,
        max_length=10
    )

    purpose = fields.CharEnumField(
        enum_type=CodePurpose,
        max_length=50
    )

    code_hash = fields.CharField(max_length=255)
    attempts = fields.IntField(default=0)
    max_attempts = fields.IntField(default=5)

    expires_at = fields.DatetimeField()
    used_at = fields.DatetimeField(null=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "verification_codes"
        indexes = [
            ("destination", "purpose"),
            ("expires_at",),
        ]

    @property
    def is_expired(self) -> bool:
        return self.expires_at < datetime.now(UTC)

    @property
    def is_used(self) -> bool:
        return self.used_at is not None
    