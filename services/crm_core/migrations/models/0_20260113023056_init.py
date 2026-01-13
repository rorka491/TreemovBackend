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
CREATE TABLE IF NOT EXISTS "organization_member" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "role_id" INT NOT NULL REFERENCES "roles" ("id") ON DELETE CASCADE,
    "user_profile_id" INT REFERENCES "profile" ("id") ON DELETE CASCADE
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
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "org_member_id" INT NOT NULL REFERENCES "organization_member" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "role_permissions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "permission_id" INT NOT NULL REFERENCES "permissions" ("id") ON DELETE CASCADE,
    "role_id" INT NOT NULL REFERENCES "roles" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_role_permis_role_id_6a25fe" UNIQUE ("role_id", "permission_id")
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
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "org_member_id" INT NOT NULL REFERENCES "organization_member" ("id") ON DELETE CASCADE
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
CREATE TABLE IF NOT EXISTS "student_group_members" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "group_id" INT NOT NULL REFERENCES "student_group" ("id") ON DELETE CASCADE,
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "student_id" INT NOT NULL REFERENCES "students" ("id") ON DELETE CASCADE
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
    "employee_id" INT NOT NULL REFERENCES "employee" ("id") ON DELETE CASCADE,
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
