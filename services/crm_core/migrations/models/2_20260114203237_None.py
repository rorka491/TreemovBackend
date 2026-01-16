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
    "pathronamic" VARCHAR(255) NOT NULL
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
    "erJF/98vLr/2p+lpA="
)
