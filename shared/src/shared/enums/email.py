from enum import Enum
from .base import CodePurpose

class EmailCodePurpose(CodePurpose):
    login = "login"
    verify_email = "verify_email"
    reset_password = "reset_password"


class DeliveryChannel(str, Enum):
    email = "email"
    sms = "sms"

