from fastapi import APIRouter, FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.api.router import router
from src.core.db import TORTOISE_ORM

app = FastAPI()

app.include_router(router)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True
)

