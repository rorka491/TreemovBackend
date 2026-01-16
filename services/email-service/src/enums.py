from typing import Mapping
from enum import Enum
from shared.enums.queue import QueueEnum
from shared.enums.email import EmailCodePurpose







class DeliveryChannel(str, Enum):
    email = "email"
    sms = "sms"
