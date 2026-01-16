import pytest_asyncio
from tortoise import Tortoise
from app.core.db import TORTOISE_ORM
from app.models.lessons import Lesson, PeriodLesson

@pytest_asyncio.fixture(scope="session", autouse=True)
async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    yield
    await Tortoise.close_connections()

@pytest_asyncio.fixture(autouse=True)
async def cleanup_tables():
    await Lesson.all().delete()
    await PeriodLesson.all().delete()
    yield
    await Lesson.all().delete()
    await PeriodLesson.all().delete()
    await Tortoise.close_connections() 


