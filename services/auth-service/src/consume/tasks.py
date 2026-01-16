import asyncio
from src.consume.consumers import email_regitser_verifed_consume
from src.consume.handlers import email_verifed_register_handler
from shared.payload import EmailVerifiedPayload


async def main_consume_tasks():
    await email_regitser_verifed_consume.connect()
    task1 = asyncio.create_task(
        email_regitser_verifed_consume.consume(
            email_verifed_register_handler, 
            EmailVerifiedPayload
        )
    )

    await asyncio.gather(task1)