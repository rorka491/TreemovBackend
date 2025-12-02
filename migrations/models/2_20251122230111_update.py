from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "department" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(100) NOT NULL,
    "code" INT NOT NULL
);
        CREATE TABLE IF NOT EXISTS "employee" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(100) NOT NULL,
    "surname" VARCHAR(100) NOT NULL,
    "patronymic" VARCHAR(100),
    "email" VARCHAR(255),
    "department_id" INT REFERENCES "department" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "teacher" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "employee_id" INT NOT NULL UNIQUE REFERENCES "employee" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "classroom" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(100) NOT NULL,
    "floor" INT,
    "building" VARCHAR(100)
);
        CREATE TABLE IF NOT EXISTS "subject" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(100) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "student_group" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(255) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "lesson_schedule_lesson" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(200) NOT NULL,
    "start_time" TIMETZ,
    "end_time" TIMETZ,
    "date" DATE NOT NULL,
    "week_day" INT NOT NULL,
    "is_canceled" BOOL NOT NULL DEFAULT False,
    "is_completed" BOOL NOT NULL DEFAULT False,
    "duration" INT NOT NULL,
    "comment" VARCHAR(200),
    "classroom_id" INT REFERENCES "classroom" ("id") ON DELETE CASCADE,
    "student_group_id" INT REFERENCES "student_group" ("id") ON DELETE CASCADE,
    "subject_id" INT REFERENCES "subject" ("id") ON DELETE CASCADE,
    "teacher_id" INT REFERENCES "teacher" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "student" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(100) NOT NULL,
    "surname" VARCHAR(100) NOT NULL,
    "progress" DECIMAL(5,2) NOT NULL DEFAULT 0,
    "birthday" DATE NOT NULL,
    "score" INT NOT NULL DEFAULT 0
);
        CREATE TABLE "student_group_student" (
    "student_id" INT NOT NULL REFERENCES "student" ("id") ON DELETE CASCADE,
    "student_group_id" INT NOT NULL REFERENCES "student_group" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "student_group_student";
        DROP TABLE IF EXISTS "student_group";
        DROP TABLE IF EXISTS "lesson_schedule_lesson";
        DROP TABLE IF EXISTS "subject";
        DROP TABLE IF EXISTS "teacher";
        DROP TABLE IF EXISTS "student";
        DROP TABLE IF EXISTS "employee";
        DROP TABLE IF EXISTS "department";
        DROP TABLE IF EXISTS "classroom";"""


MODELS_STATE = (
    "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"
)
