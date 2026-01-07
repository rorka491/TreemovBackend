from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "lesson_schedule_lesson" RENAME TO "lesson";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "lesson" RENAME TO "lesson_schedule_lesson";"""


MODELS_STATE = (
    "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"
    "aCPwjsbaP1lcB5eTfpap8gv0n/vfAK7/B4MgGZU="
)
