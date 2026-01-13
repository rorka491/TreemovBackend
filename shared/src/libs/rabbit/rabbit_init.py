import asyncio
import aio_pika
from aio_pika import ExchangeType
from shared.enums.queue import QueueEnum


RABBIT_URL = "amqp://guest:guest@localhost/"
EXCHANGE_NAME = "amq.direct"
QUEUES = list(QueueEnum)


async def init_rabbit(
    url: str, 
    queues: list, 
    exchange_name: str = EXCHANGE_NAME
):
    connection = await aio_pika.connect_robust(url)
    async with connection:
        channel = await connection.channel()

        exchange = await channel.get_exchange(exchange_name)
        for queue_name in queues:
            queue = await channel.declare_queue(
                queue_name,
                durable=True
            )
            await queue.bind(exchange)

        print("RabbitMQ infrastructure initialized")

if __name__ == "__main__":
    asyncio.run(init_rabbit())