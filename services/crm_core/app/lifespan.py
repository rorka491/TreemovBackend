from fastapi import FastAPI
import asyncio
from pathlib import Path
from contextlib import asynccontextmanager
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from app.core.db import TORTOISE_ORM
from app.core.config import BASE_DIR
from app.consume.tasks import user_created_consumer_task
from app.core.config import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas(safe=True)

    logger.warning('start user_created_consumer_task')
    task = asyncio.create_task(user_created_consumer_task())
    yield
    task.cancel()
    await Tortoise.close_connections()
