from app.core.config import DB_NAME, DB_PASSWORD, DB_USER

TORTOISE_ORM = {
    "connections": {"default": f"postgres://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"},
    "apps": {
        "models": {
            "models": [
                "app.models",
                "aerich.models",
            ],
            "default_connection": "default",
        }
    },
}