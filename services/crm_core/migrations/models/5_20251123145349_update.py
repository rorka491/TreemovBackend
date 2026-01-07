from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "classroom" ADD "org_id" INT NOT NULL;
        ALTER TABLE "department" ADD "org_id" INT NOT NULL;
        ALTER TABLE "employee" ADD "org_id" INT NOT NULL;
        ALTER TABLE "lesson" ADD "org_id" INT NOT NULL;
        ALTER TABLE "organization" ADD "org_id" INT NOT NULL;
        ALTER TABLE "student" ADD "org_id" INT NOT NULL;
        ALTER TABLE "student_group" ADD "org_id" INT NOT NULL;
        ALTER TABLE "subject" ADD "org_id" INT NOT NULL;
        ALTER TABLE "teacher" ADD "org_id" INT NOT NULL;
        ALTER TABLE "user" ADD "org_id" INT NOT NULL;
        ALTER TABLE "classroom" ADD CONSTRAINT "fk_classroo_organiza_e19c1bdf" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;
        ALTER TABLE "department" ADD CONSTRAINT "fk_departme_organiza_c9a6dcf2" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;
        ALTER TABLE "employee" ADD CONSTRAINT "fk_employee_organiza_222fbe09" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;
        ALTER TABLE "lesson" ADD CONSTRAINT "fk_lesson_organiza_6361741b" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;
        ALTER TABLE "organization" ADD CONSTRAINT "fk_organiza_organiza_2938701b" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;
        ALTER TABLE "student" ADD CONSTRAINT "fk_student_organiza_faf16e29" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;
        ALTER TABLE "student_group" ADD CONSTRAINT "fk_student__organiza_cbdf81fa" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;
        ALTER TABLE "subject" ADD CONSTRAINT "fk_subject_organiza_e23aabd5" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;
        ALTER TABLE "teacher" ADD CONSTRAINT "fk_teacher_organiza_9468bb4e" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;
        ALTER TABLE "user" ADD CONSTRAINT "fk_user_organiza_3ed393cd" FOREIGN KEY ("org_id") REFERENCES "organization" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "student_group" DROP CONSTRAINT IF EXISTS "fk_student__organiza_cbdf81fa";
        ALTER TABLE "organization" DROP CONSTRAINT IF EXISTS "fk_organiza_organiza_2938701b";
        ALTER TABLE "department" DROP CONSTRAINT IF EXISTS "fk_departme_organiza_c9a6dcf2";
        ALTER TABLE "classroom" DROP CONSTRAINT IF EXISTS "fk_classroo_organiza_e19c1bdf";
        ALTER TABLE "employee" DROP CONSTRAINT IF EXISTS "fk_employee_organiza_222fbe09";
        ALTER TABLE "teacher" DROP CONSTRAINT IF EXISTS "fk_teacher_organiza_9468bb4e";
        ALTER TABLE "subject" DROP CONSTRAINT IF EXISTS "fk_subject_organiza_e23aabd5";
        ALTER TABLE "student" DROP CONSTRAINT IF EXISTS "fk_student_organiza_faf16e29";
        ALTER TABLE "lesson" DROP CONSTRAINT IF EXISTS "fk_lesson_organiza_6361741b";
        ALTER TABLE "user" DROP CONSTRAINT IF EXISTS "fk_user_organiza_3ed393cd";
        ALTER TABLE "user" DROP COLUMN "org_id";
        ALTER TABLE "lesson" DROP COLUMN "org_id";
        ALTER TABLE "student" DROP COLUMN "org_id";
        ALTER TABLE "subject" DROP COLUMN "org_id";
        ALTER TABLE "teacher" DROP COLUMN "org_id";
        ALTER TABLE "employee" DROP COLUMN "org_id";
        ALTER TABLE "classroom" DROP COLUMN "org_id";
        ALTER TABLE "department" DROP COLUMN "org_id";
        ALTER TABLE "organization" DROP COLUMN "org_id";
        ALTER TABLE "student_group" DROP COLUMN "org_id";"""


MODELS_STATE = (
    "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"
    "Gg3+SXM9uxyfphWkOMGpamLe5vTy8D8CFnxj"
)
