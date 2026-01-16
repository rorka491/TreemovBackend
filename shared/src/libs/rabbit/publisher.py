import aio_pika
from shared.enums.queue import QueueEnum 
from pydantic import BaseModel
from faststream.rabbit.fastapi import RabbitRouter
import json


class RabbitPublisher:
    def __init__(self, url: str, exchange_name: str):
        self.url = url
        self.exchange_name = exchange_name

    async def connect(self) -> None:
        self._connection = await aio_pika.connect_robust(self.url)
        self._channel = await self._connection.channel()
        self._exchange = await self._channel.get_exchange(self.exchange_name)


    async def publish(self, payload: BaseModel, queue: QueueEnum) -> None:
        if not hasattr(self, "_exchange"):
            await self.connect()
            
        message = aio_pika.Message(
            body=payload.model_dump_json().encode(),
            content_type="application/json",
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )

        await self._exchange.publish(
            message,
            routing_key=queue.value,
        )
    
    async def test_publish(self):
        if not hasattr(self, "_exchange"):
            await self.connect()
        message_body = {"message": "test"}
        message = aio_pika.Message(
            body=json.dumps(message_body).encode("utf-8"),
            content_type="application/json",
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )
        await self._exchange.publish(message, routing_key="test.queue")
    
    async def close(self) -> None:
        if hasattr(self, "_connection"):
            await self._connection.close()


