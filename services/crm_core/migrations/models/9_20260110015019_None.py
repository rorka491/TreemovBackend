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
CREATE TABLE IF NOT EXISTS "organizationmember" (
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
    "org_member_id" INT NOT NULL REFERENCES "organizationmember" ("id") ON DELETE CASCADE
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
    "org_id" INT NOT NULL REFERENCES "organization" ("id") ON DELETE CASCADE,
    "org_member_id" INT NOT NULL REFERENCES "organizationmember" ("id") ON DELETE CASCADE
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
    "q19efv0fWSYo7Q=="
)
