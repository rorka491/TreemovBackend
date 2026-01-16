from fastapi import Depends
# from src.services.code import ...
# from src.services.email import ...
from src.core.config import EMAIL_HOST, EMAIL_PASSWORD, EMAIL_USERNAME
from src.email_provider import SMTPEmailProvider, EmailProvider
from src.services.email import EmailService
from libs.rabbit.publisher import RabbitPublisher
from libs.rabbit.rabbit_init import RABBIT_URL, EXCHANGE_NAME



def get_email_provider() -> EmailProvider:
    return SMTPEmailProvider(
        host=EMAIL_HOST,
        port=587,
        username=EMAIL_USERNAME,
        password=EMAIL_PASSWORD,
    )


def get_producer():
    return RabbitPublisher(exchange_name=EXCHANGE_NAME, url=RABBIT_URL)


def get_email_service(
    provider: EmailProvider = Depends(get_email_provider),
    producer: RabbitPublisher = Depends(get_producer)
) -> EmailService:
    return EmailService(provider=provider, producer=producer)

