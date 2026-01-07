from fastapi import FastAPI
from contextlib import asynccontextmanager
from shared.rabbit.rabbit_init import init_rabbit
from app.core.config import QUEUES, EXCHANGE_NAME, RABBIT_URL

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_rabbit(exchange=EXCHANGE_NAME, url=RABBIT_URL, queues=QUEUES)
