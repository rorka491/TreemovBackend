from typing import Mapping
from enum import Enum


class CodePurpose(str, Enum):
    login = "login"
    verify_email = "verify_email"
    reset_password = "reset_password"


PurposeQueueMapping: Mapping


class DeliveryChannel(str, Enum):
    email = "email"
    sms = "sms"
