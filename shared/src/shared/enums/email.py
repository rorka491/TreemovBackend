from typing import Mapping
from shared.enums.queue import QueueEnum
from enum import Enum
from .base import CodePurpose

class EmailCodePurpose(CodePurpose):
    verify_email = "verify_email"
    login = "login"
    reset_password = "reset_password"

PurposeQueueMapping: Mapping[EmailCodePurpose, QueueEnum] = {
    EmailCodePurpose.verify_email: QueueEnum.EMAIL_REGISTER_VERIFIED, 
    EmailCodePurpose.login: QueueEnum.EMAIL_LOGIN_VERIFIED
}


class DeliveryChannel(str, Enum):
    email = "email"
    sms = "sms"

