import re
from tortoise import Tortoise


def clear_ijection(name: str) -> str:
    if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name):
        raise ValueError("Invalid schema name")
    return f'{name}'


# async def set_schema_for_models(schema_name: str):
#     from app.models import Employee, Student    

#     for model in [Employee, Student]:
#         model.Meta.schema = schema_name


# async def create_schema(schema_name: str):
#     conn = Tortoise.get_connection("default")
#     schema_safe = clear_ijection(schema_name)

#     await conn.execute_script(f"CREATE SCHEMA IF NOT EXISTS {schema_safe};")
#     await conn.execute_query(f"SET search_path TO {schema_safe}")
#     await set_schema_for_models(schema_safe)
#     await Tortoise.generate_schemas(safe=True)
