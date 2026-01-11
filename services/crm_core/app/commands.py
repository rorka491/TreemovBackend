from tortoise import Tortoise
from app.core.db import TORTOISE_ORM
from app.core.config import BASE_DIR


async def seed():
    sql_path = BASE_DIR / "sql" / "seed.sql"

    if not sql_path.exists():
        print("seed.sql not found")
        return

    await Tortoise.init(config=TORTOISE_ORM)

    try:
        conn = Tortoise.get_connection("default")
        script = sql_path.read_text(encoding="utf-8")
        await conn.execute_script(script)
        print("Seed applied successfully")
    finally:
        await Tortoise.close_connections()



