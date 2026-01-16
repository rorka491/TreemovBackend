from shared import EventFactory
from shared.rabbit.publisher import RabbitPublisher




publisher = RabbitPublisher(
    url="amqp://guest:guest@localhost:5672/",
    exchange_name="events",
)