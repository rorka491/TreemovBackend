from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "profilerole" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "profile_id" INT NOT NULL REFERENCES "profile" ("id") ON DELETE CASCADE,
    "role_id" INT NOT NULL REFERENCES "roles" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "profilerole";"""


MODELS_STATE = (
    "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"
    "XWr//18uv/dpjg6g=="
)
