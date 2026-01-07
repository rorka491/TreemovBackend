from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "organization" DROP CONSTRAINT IF EXISTS "fk_organiza_organiza_2938701b";
        ALTER TABLE "organization" DROP COLUMN "org_id";
        ALTER TABLE "user" ALTER COLUMN "org_id" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "org_id" SET NOT NULL;
        ALTER TABLE "organization" ADD "org_id" INT NOT NULL;
        ALTER TABLE "organization" ADD CONSTRAINT "fk_organiza_organiza_2938701b" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;"""


MODELS_STATE = (
    "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"
)
