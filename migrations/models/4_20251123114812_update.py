from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE UNIQUE INDEX IF NOT EXISTS "uid_organizatio_title_841a2f" ON "organization" ("title");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "organization" DROP CONSTRAINT IF EXISTS "organization_title_key";
        DROP INDEX IF EXISTS "uid_organizatio_title_841a2f";"""


MODELS_STATE = (
    "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"
    "oY3AOxpr/2RxHVxO+lmmyi/Qf+5/A7j+H3OSGP8="
)
