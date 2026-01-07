from fastapi import FastAPI, Request, APIRouter
from tortoise.contrib.fastapi import register_tortoise
from app.core.db import TORTOISE_ORM
from app.middleware import TenantMiddleware
from app.api.routers import router
from app.lifespan import lifespan

app = FastAPI(lifespan=lifespan)

app.include_router(router)
app.add_middleware(TenantMiddleware)


register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)

