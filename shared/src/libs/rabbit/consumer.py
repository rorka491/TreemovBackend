import json
import aio_pika
from typing import Type
from shared.contracts.base import Event, QueueEnum
from shared.contracts.maping import EVENT_PAYLOAD_MAP

class RabbitConsumer:
    def __init__(
        self,
        url: str,
        exchange_name: str,
        queue_name: str,
        binding_keys: list[str],
    ):
        self.url = url
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.binding_keys = binding_keys

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.url)
        self.channel = await self.connection.channel()

        self.exchange = await self.channel.declare_exchange(
            self.exchange_name,
            aio_pika.ExchangeType.TOPIC,
            durable=True,
        )

        self.queue = await self.channel.declare_queue(
            self.queue_name,
            durable=True,
        )

        for key in self.binding_keys:
            await self.queue.bind(self.exchange, routing_key=key)

    async def handle_message(self, message: aio_pika.IncomingMessage):
        async with message.process():
            data = json.loads(message.body.decode())

            event_type = QueueEnum(data["event"])
            payload_cls: Type = EVENT_PAYLOAD_MAP[event_type]
            payload = payload_cls.model_validate(data["payload"])

            event = Event(
                event=event_type,
                payload=payload,
                occurred_at=data["occurred_at"],
                version=data["version"],
            )

            print("Received event:", event)

    async def start(self):
        await self.queue.consume(self.handle_message)
        print(f"Listening on queue: {self.queue_name}")



