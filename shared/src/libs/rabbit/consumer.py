import json
import aio_pika
from typing import Callable, Awaitable
from pydantic import BaseModel
from shared.enums.queue import QueueEnum
from app.core.config import logger
import asyncio


class RabbitConsumer:
    def __init__(self, url: str, queue: QueueEnum):
        self.url = url
        self.queue_name = queue.value
        self._connection = None
        self._channel = None
        self._queue = None

    async def connect(self) -> None:
        self._connection = await aio_pika.connect_robust(self.url)
        self._channel = await self._connection.channel()
        self._queue = await self._channel.declare_queue(
            self.queue_name,
            durable=True
        )

    # async def consume(self, callback: Callable[[BaseModel], None], model: type[BaseModel]):
    #     """
    #     callback: функция, которая принимает объект model
    #     model: Pydantic модель, в которую десериализуем сообщение
    #     """
    #     async with self._connection:
    #         async with self._queue.iterator() as queue_iter:
    #             async for message in queue_iter:
    #                 async with message.process():
    #                     data = message.body.decode()
    #                     obj = model.model_validate(data)
    #                     await callback(obj)

    async def consume(self, callback: Callable[[BaseModel], Awaitable[None]], model: type[BaseModel]):
        async with self._connection:
            async with self._queue.iterator() as queue_iter:
                try:
                    async for message in queue_iter:
                        async with message.process():
                            data = message.body.decode()
                            try:
                                obj = model.model_validate_json(data)
                                await callback(obj)
                            except Exception as e:
                                logger.exception("Failed to process message")
                except asyncio.CancelledError:
                    logger.info("Consumer loop cancelled")
                    raise