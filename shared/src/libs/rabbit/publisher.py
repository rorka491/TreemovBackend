import aio_pika
from shared.contracts.base import Event
from faststream.rabbit.fastapi import RabbitRouter



class RabbitPublisher:
    def __init__(self, url: str, exchange_name: str):
        self.url = url
        self.exchange_name = exchange_name
        self.connection = None
        self.channel = None
        self.exchange = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.url)
        self.channel = await self.connection.channel()

        self.exchange = await self.channel.declare_exchange(
            self.exchange_name,
            aio_pika.ExchangeType.TOPIC,
            durable=True,
        )

    async def publish(self, event: Event):
        message = aio_pika.Message(
            body=event.model_dump_json().encode(),
            content_type="application/json",
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )

        routing_key = event.event_type.value
        await self.exchange.publish(message, routing_key=routing_key)

    async def close(self):
        await self.connection.close()


