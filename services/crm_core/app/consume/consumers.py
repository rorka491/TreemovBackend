from libs.rabbit.consumer import RabbitConsumer
from shared.enums.queue import QueueEnum
from shared.config import RABBIT_SERVICE_URL, RABBIT_SERVICE_URL_DOCKER



user_created_consume = RabbitConsumer(
    url=RABBIT_SERVICE_URL,
    queue=QueueEnum.USER_CREATED
)