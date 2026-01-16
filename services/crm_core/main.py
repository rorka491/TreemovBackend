import asyncio
from fastapi import FastAPI, Request, APIRouter
from tortoise.contrib.fastapi import register_tortoise
from app.core.db import TORTOISE_ORM
# from app.middleware import TenantMiddleware
from app.api.routers import router
from app.consume.tasks import user_created_consumer_task


app = FastAPI()

app.include_router(router)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)

@app.on_event("startup")
async def startup():
    asyncio.create_task(user_created_consumer_task())

