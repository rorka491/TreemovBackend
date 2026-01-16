from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" DROP CONSTRAINT IF EXISTS "users_username_key";
        DROP INDEX IF EXISTS "uid_users_usernam_266d85";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE UNIQUE INDEX IF NOT EXISTS "uid_users_usernam_266d85" ON "users" ("username");"""


MODELS_STATE = (
    "eJztl1tv2jAUx78KylMndRMEuiLeAmMaUwGpLdOkropMYoKFY6ex04sqvntt535DUJUxNN"
    "7IuSTn/HR8/uZVc6kNMfti2C4iWq/xqhHgQvEj7zhvaMDzUrM0cDDHKhIkIXPGfWBxYVwA"
    "zKAw2ZBZPvI4ovLtJMBYGqklAhFxUlNA0EMATU4dyJfQF467e2FGxIbPkMWP3spcIIjtXK"
    "HIlt9WdpO/eMo2Ivy7CpRfm5sWxYFL0mDvhS8pSaIR4dLqQAJ9wKF8PfcDWb6sLmoz7iis"
    "NA0JS8zk2HABAswz7W7JwKJE8hPVMNWgI7/yWW91Ljvd9tdOV4SoShLL5TpsL+09TFQEJr"
    "faWvkBB2GEwphyCxj01e8SvcES+NX4sjkFiKL0IsQY2UEpuuDZxJA4fCke2/oGZL+M68EP"
    "4/qsrX+SnVAxyuGATyKPrlySakrRA4w9Ub9iBuspZnM+hmJsSDGmB3AfHFt6dwuQIqqWpP"
    "LlUSJmiuWBHismsk8phoDUnOlsXoHnXCTuC2gyqe8CuoFffzq9kkW7jD1gZRjdFjjOxv2h"
    "AKzwiiDEYXro5aZcrDJnXhrmwFo9Ad82Sx6q07rYssvV3aIFEOAoQrJP2VWkHDOm9nhJUZ"
    "R9o6DILcNOgnISlGNYhfrFxRarUETVrkLly69C6AKEd+GYJLwLYjRoBxLlvRA86fKH6bIv"
    "tLca45AErkI5EjUBYsES0jj37+FUK0UrAdWMb+PRpNdQf1b+kNnN8LrXSEJ3xLzNvNZPa2"
    "lWj+3is6sW/283HwP6yFpW3X0iz8bbD0hjTtefI7r+PIpLqyxpB8HJpByn3uxFuuXR2AFi"
    "FH6cAFvN5jaC3WzWC7b05QGKL3IYnsE8xJ8300k1xExKAeSMiAbvbGTx8wZGjN//m1g3UJ"
    "Rd50Qlhnc2Nn4XuQ6upn1FgTLu+Oot6gX9Q8vL+g02BucH"
)
