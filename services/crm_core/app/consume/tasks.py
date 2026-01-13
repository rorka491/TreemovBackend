import asyncio
from typing import Awaitable, Callable
from app.consume.consumers import user_created_consume
from app.consume.handlers import handle_user_created
from app.core.config import logger
from shared.payload import UserCreatedPayload



async def user_created_consumer_task():
    await user_created_consume.connect()
    await user_created_consume.consume(handle_user_created, UserCreatedPayload)



