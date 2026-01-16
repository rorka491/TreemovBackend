import asyncio
from fastapi import FastAPI, Request, APIRouter
from tortoise.contrib.fastapi import register_tortoise
from app.core.db import TORTOISE_ORM
from app.api.routers import router
from app.lifespan import lifespan 

app = FastAPI(lifespan=lifespan)


register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)

app.include_router(router)

# @app.on_event("startup")
# async def startup():
#     logger.info(f"{GREEN} task_started {RESET}")
#     asyncio.create_task(user_created_consumer_task())



