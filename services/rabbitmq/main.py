import asyncio
from src.config import RABBIT_URL
from libs.rabbit.rabbit_init import init_rabbit, QUEUES, EXCHANGE_NAME
from shared.config import RABBIT_SERVICE_URL_DOCKER

async def main():
    return await init_rabbit(queues=QUEUES, url=RABBIT_SERVICE_URL_DOCKER)


if __name__ == "__main__":
    asyncio.run(main())



