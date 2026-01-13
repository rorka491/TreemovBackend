from app.consume.consumers import user_created_consume
from app.consume.handlers import handle_user_created
from shared.payload import UserCreatedPayload


async def user_created_consumer_task():
    await user_created_consume.connect()
    await user_created_consume.consume(handle_user_created, UserCreatedPayload)
    
