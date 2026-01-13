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
    def get_payload_cls(cls, queue: QueueEnum) -> type[BaseModel] | None:
        return cls._mapping.get(queue)

    @classmethod
    def get_payload_dict(cls, payload_cls: type[BaseModel], payload_obj: BaseModel) -> dict:
        return payload_obj.model_dump(
            include=payload_cls.model_fields.keys()
        )

    @classmethod
    def build_payload(cls, queue: QueueEnum, payload_obj: BaseModel) -> BaseModel:
        payload_cls = cls.get_payload_cls(queue)
        if not payload_cls:
            return None
        payload_dict = cls.get_payload_dict(payload_cls=payload_cls, payload_obj=payload_obj)
        return payload_cls(**payload_dict)


