from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "admin" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(32) NOT NULL UNIQUE,
    "password" VARCHAR(128) NOT NULL,
    "is_active" BOOL NOT NULL DEFAULT True
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(255) NOT NULL UNIQUE,
    "email" VARCHAR(255) UNIQUE,
    "password" VARCHAR(128) NOT NULL,
    "role" VARCHAR(5) NOT NULL DEFAULT 'user',
    "is_active" BOOL NOT NULL DEFAULT False
);
COMMENT ON COLUMN "users"."role" IS 'ADMIN: admin\nUSER: user';
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
    "eJztl1tv2jAUx78KylMndRMEuiLeAmMaUwGpLdOkropMYoKFY6ex04sqvntt535DUJW1bL"
    "yRc7HP+enYf/OsudSGmH0xbBcRrdd41ghwofiRd5w2NOB5qVkaOJhjFQmSkDnjPrC4MC4A"
    "ZlCYbMgsH3kcUbk6CTCWRmqJQESc1BQQdBdAk1MH8iX0hePmVpgRseEjZPGntzIXCGI7Vy"
    "iy5d7KbvInT9lGhH9XgXK3uWlRHLgkDfae+JKSJBoRLq0OJNAHHMrluR/I8mV1UZtxR2Gl"
    "aUhYYibHhgsQYJ5pd0sGFiWSn6iGqQYductnvdU573TbXztdEaIqSSzn67C9tPcwURGYXG"
    "tr5QcchBEKY8otYNBXv0v0BkvgV+PL5hQgitKLEGNk70rRBY8mhsThS/HZ1jcg+2VcDn4Y"
    "lydt/ZPshIpRDgd8Enl05ZJUU4oeYOyB+hUzWE8xm/M2FGNDijE9gPvg2NK7W4AUUbUklS"
    "+PEjFTXB7ovmIi+5RiCEjNmc7mFXjOReK+gCaT+iqgG/j1p9MLWbTL2B1WhtF1geNs3B8K"
    "wAqvCEIcpode3pSLVebMS8McWKsH4NtmyUN1Whdbdrm6W7QAAhxFSPYpu4qUY8bUPV5SFG"
    "XfKCjylmFHQTkKyscXFP3sbIuLUETVXoTKl78IoQsQ3oVikvAqhBGgf4ngUZXfTJV9obzV"
    "GIckcBXKkagJEAuWkMa5fw+nulC0ElDN+DYeTXoN9VflD5ldDS97jSR0R8zbzGv9tJZm9d"
    "CePbsq8f/27jGgj6xl1csn8mx8+4A05vj4OaDHz714ssqSdhCcTMph6s1epFsejR0gRuGH"
    "CbDVbG4j2M1mvWBLXx6g2JHD8AzmIf68mk6qIWZSCiBnRDR4YyOLnzYwYvz2Y2LdQFF2nR"
    "OVGN7J2Phd5Dq4mPYVBcq446tV1AL995aX9QsM4uZx"
)
