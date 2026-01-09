from fastapi import FastAPI
from contextlib import asynccontextmanager
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from app.core.db import TORTOISE_ORM
from app.core.config import BASE_DIR
from pathlib import Path




@asynccontextmanager
async def lifespan(app: FastAPI):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True,
    )
    conn = Tortoise.get_connection("default")
    sql_path = BASE_DIR / "sql" / "seed.sql"
    script = Path(sql_path).read_text(encoding="utf-8")

    if sql_path.exists():
        conn = Tortoise.get_connection("default")
        await conn.execute_script(script)

    yield
