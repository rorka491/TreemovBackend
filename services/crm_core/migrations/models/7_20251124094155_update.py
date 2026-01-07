from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP CONSTRAINT IF EXISTS "fk_user_organiza_3ed393cd";
        ALTER TABLE "user" DROP COLUMN "org_id";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "org_id" INT;
        ALTER TABLE "user" ADD CONSTRAINT "fk_user_organiza_3ed393cd" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;"""


MODELS_STATE = (
    "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"
)
