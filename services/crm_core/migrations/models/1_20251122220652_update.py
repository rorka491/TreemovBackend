from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "organization" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(255) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "login" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "role" VARCHAR(7) NOT NULL
);
COMMENT ON COLUMN "user"."role" IS 'ADMIN: Admin\nMANAGER: Manager\nTEACHER: Teacher';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user";
        DROP TABLE IF EXISTS "organization";"""


MODELS_STATE = (
    "eJztmG1P2zAQx79KlFdMYgg6oIh3oXSj09pOELaJB0Vu4qYWjh1sZ9ChfvfZzoPTtI3oRA"
    "Voedf+7y6++12Su/bJjmgAMd8ZshAQ9AcIRIl9bD3ZBERQflhq37ZsEMfGqgQBRlgH0Krn"
    "iAsGfCFtY4A5lFIAuc9QnJ1FEoyVSH3piEhopISg+wR6goZQTCCThutbKSMSwEfI86/xnT"
    "dGEAdzaaNAna11T0xjrfWI+Kwd1Wkjz6c4iYhxjqdiQknhjYhQaggJZEBAdXnBEpW+yi6r"
    "Nq8ozdS4pCmWYgI4BgkWpXKfycCnRPGT2XBdYKhO+dja22/vH3063D+SLjqTQmnP0vJM7W"
    "mgJjBw7Zm2AwFSD43RcPMZVMV6QCzyO5UWgSK4HOJ8ZAVmkIXu5B+qaHOQdWxzwcA1N9QL"
    "0ZU1BEOCp1njalC6vX73wnX631UlEef3WCNy3K6ytLQ6rahbhx+UTuXjkD4rxUWsnz33zF"
    "JfravhoKsJUi5Cpk80fu6VrXICiaAeoQ8eCEr3WK7mYKSnaWwSB//Y2PnIprGv2tgsedNX"
    "gQSGiy3tTABb3s4ioNJJieuN9i4Cjx6GJBQT9Z47OKhp3g/nvHPmnG9Jr0pHBpmpldpmMz"
    "U6xnell6ASRsC/ewAs8BYstEVX+S6aolZUVQABocajilQVZIP1kuvBtjBwtV47aJPcoxmw"
    "zYBt3sPNgG0au4kBi2mIyDoDtgh4mQG78RfeZsZrGWEMOH+gbMnEWE2xHPOfbypllDACCK"
    "/DsQho7sYMIaOrFuYuSSJNsSdzAsSHCzTz2Fe+I23ntN8bHFtOECFyQ/rOwPnSPT+2+nrL"
    "ZDfE7TqdM6W4EPiTdE9cF37dnpOjb68E335DO7YDGfIn9pItO7PU7tnA+DSb9jvatH9Dxr"
    "P/IJ/7siyFNDOnAKkejTUgZu7vE+De7u4zAEqvlQC1bR6gPFFAsuR3wdeL4WDFjz0TUgF5"
    "SWSB1wHyxbaFERe3bxNrDUVV9dzun8Pb6ju/qlw734Yn1aVeXeDktcfL7C/sbA03"
)
