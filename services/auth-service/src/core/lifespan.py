import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from passlib.hash import bcrypt
from src.models import User
from tortoise.exceptions import DoesNotExist
import os
from src.core.config import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_USERNAME
from src.core.config import hasher 
from src.enums import UserRole
from src.consume.tasks import main_consume_tasks
from libs.logger import logger, GREEN, RESET



@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"{GREEN} task_started {RESET}")
    consumer_task = asyncio.create_task(main_consume_tasks())
    try:
        await User.get(username=ADMIN_USERNAME)
    except DoesNotExist:
        await User.create(
            username=ADMIN_USERNAME,
            email=ADMIN_EMAIL,
            password=hasher.hash(ADMIN_PASSWORD),
            role=UserRole.ADMIN.value,
            is_active=True
        )
        logger.info(f"{GREEN} Admin created {RESET}")
    yield
    consumer_task.cancel()