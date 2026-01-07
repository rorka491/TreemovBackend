from pydantic import BaseModel
from typing import Mapping
from shared.enums.queue import QueueEnum
from shared.payload import EmailVerifiedPayload, UserCreatedPayload
import logging

logger = logging.getLogger(__name__)

QUEUE_PAYLOAD_MAPPING: Mapping["QueueEnum", "BaseModel"] = {
    QueueEnum.USER_CREATED: UserCreatedPayload,
    QueueEnum.EMAIL_REGISTER_VERIFIED: EmailVerifiedPayload,
    QueueEnum.EMAIL_LOGIN_VERIFIED: EmailVerifiedPayload,
}



class EventPayloadMapper:
    _mapping = QUEUE_PAYLOAD_MAPPING

    @classmethod
    def get_payload_cls(cls, queue_type: QueueEnum) -> type[BaseModel] | None:
        return cls._mapping.get(queue_type)

    @classmethod
    def build_payload(cls, queue_type: QueueEnum, payload_obj: BaseModel) -> dict | None:
        payload_cls = cls.get_payload_cls(queue_type)
        if not payload_cls:
            return None

        return payload_obj.model_dump(
            include=payload_cls.model_fields.keys()
        )




