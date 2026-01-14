from libs.rabbit.publisher import RabbitPublisher
from libs.rabbit.rabbit_init import EXCHANGE_NAME
from shared.enums.queue import QueueEnum
from shared.config import RABBIT_SERVICE_URL, RABBIT_SERVICE_URL_DOCKER


producer = RabbitPublisher(
    url=RABBIT_SERVICE_URL,
    exchange_name=EXCHANGE_NAME
)