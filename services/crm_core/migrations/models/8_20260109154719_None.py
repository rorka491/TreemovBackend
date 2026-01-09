from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "organization" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(255) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "classroom" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(100) NOT NULL,
    "floor" INT,
    "building" VARCHAR(100),
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "department" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(100) NOT NULL,
    "code" INT NOT NULL,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "employee" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(100) NOT NULL,
    "surname" VARCHAR(100) NOT NULL,
    "patronymic" VARCHAR(100),
    "email" VARCHAR(255),
    "department_id" INT REFERENCES "department" ("id") ON DELETE CASCADE,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "permissions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "code" VARCHAR(100) NOT NULL UNIQUE,
    "name" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "profile" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL,
    "is_system_admin" BOOL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "surname" VARCHAR(255) NOT NULL,
    "pathronamic" VARCHAR(255) NOT NULL,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "invites" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "status" VARCHAR(50) NOT NULL,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "profile_id" INT NOT NULL REFERENCES "profile" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "roles" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "code" VARCHAR(50) NOT NULL UNIQUE,
    "title" VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "profile_roles" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "profile_id" INT NOT NULL REFERENCES "profile" ("id") ON DELETE CASCADE,
    "role_id" INT NOT NULL REFERENCES "roles" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "rolepermission" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "permission_id" INT NOT NULL REFERENCES "permissions" ("id") ON DELETE CASCADE,
    "role_id" INT NOT NULL REFERENCES "roles" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_rolepermiss_role_id_c63292" UNIQUE ("role_id", "permission_id")
);
CREATE TABLE IF NOT EXISTS "students" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(100) NOT NULL,
    "surname" VARCHAR(100) NOT NULL,
    "progress" DECIMAL(5,2) NOT NULL DEFAULT 0,
    "birthday" DATE NOT NULL,
    "score" INT NOT NULL DEFAULT 0,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "accruals" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "amount" INT NOT NULL DEFAULT 0,
    "comment" VARCHAR(255) NOT NULL,
    "category" VARCHAR(13) NOT NULL DEFAULT 'attendance',
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "student_id" INT NOT NULL REFERENCES "students" ("id") ON DELETE CASCADE,
    "teacher_id" INT NOT NULL REFERENCES "profile" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "accruals"."category" IS 'ATTENDANCE: attendance\nPARTICIPATION: participation\nBEHAVIOR: behavior\nACHIEVEMENTS: achievements\nHOMEWORK: homework';
CREATE TABLE IF NOT EXISTS "student_group" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(255) NOT NULL,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "subject" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(100) NOT NULL,
    "color" VARCHAR(7) NOT NULL,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "teacher" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(100) NOT NULL,
    "surname" VARCHAR(100) NOT NULL,
    "patronymic" VARCHAR(100),
    "email" VARCHAR(255),
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "lesson" (
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
    "classroom_id" INT REFERENCES "classroom" ("id") ON DELETE SET NULL,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "student_group_id" INT REFERENCES "student_group" ("id") ON DELETE CASCADE,
    "subject_id" INT REFERENCES "subject" ("id") ON DELETE CASCADE,
    "teacher_id" INT REFERENCES "teacher" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "lesson"."start_time" IS 'Please use the following format: <em>YYYY-MM-DD</em>.';
COMMENT ON COLUMN "lesson"."end_time" IS 'Please use the following format: <em>YYYY-MM-DD</em>.';
CREATE TABLE IF NOT EXISTS "attendances" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "was_present" BOOL NOT NULL DEFAULT False,
    "comment" TEXT,
    "lesson_id" INT NOT NULL REFERENCES "lesson" ("id") ON DELETE CASCADE,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "student_id" INT NOT NULL REFERENCES "students" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "grades" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "value" INT DEFAULT 0,
    "comment" TEXT,
    "grade_date" DATE,
    "lesson_id" INT NOT NULL REFERENCES "lesson" ("id") ON DELETE CASCADE,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "student_id" INT NOT NULL REFERENCES "students" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "period_lesson" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(200) NOT NULL,
    "start_time" TIMETZ,
    "end_time" TIMETZ,
    "period" SMALLINT,
    "repeat_lessons_until_date" DATE,
    "start_date" DATE,
    "classroom_id" INT REFERENCES "classroom" ("id") ON DELETE SET NULL,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "student_group_id" INT REFERENCES "student_group" ("id") ON DELETE CASCADE,
    "subject_id" INT REFERENCES "subject" ("id") ON DELETE CASCADE,
    "teacher_id" INT REFERENCES "teacher" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "period_lesson"."start_time" IS 'Please use the following format: <em>YYYY-MM-DD</em>.';
COMMENT ON COLUMN "period_lesson"."end_time" IS 'Please use the following format: <em>YYYY-MM-DD</em>.';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "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"
)
