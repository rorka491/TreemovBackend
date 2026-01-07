from enum import Enum


class CodePurpose(str, Enum):
    login = "login"
    verify_email = "verify_email"
    reset_password = "reset_password"


class DeliveryChannel(str, Enum):
    email = "email"
    sms = "sms"


class EventType(str, Enum):
    EMAIL_CODE_SENT = "email.code.sent"
    EMAIL_VERIFIED = "email.verified"