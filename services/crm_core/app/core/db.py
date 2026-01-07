TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:1234@localhost:5432/postgres"},
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
