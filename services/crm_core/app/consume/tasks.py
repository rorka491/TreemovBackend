import asyncio
from typing import Awaitable, Callable
from app.consume.consumers import user_created_consume
from app.consume.handlers import handle_user_created
from app.core.config import logger
from shared.payload import UserCreatedPayload




async def main_consume_tasks():
    await user_created_consume.connect()
    task1 = asyncio.create_task(
        user_created_consume.consume(
            handle_user_created, 
            UserCreatedPayload
        )
    )

    await asyncio.gather(task1)