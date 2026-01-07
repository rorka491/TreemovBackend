from fastapi import Depends
# from src.services.code import ...
# from src.services.email import ...
from src.email_provider import SMTPEmailProvider, EmailProvider
from src.services.email import EmailService
from shared.rabbit.publisher import RabbitPublisher
from src.core.config import publisher 


def get_email_provider() -> EmailProvider:
    return SMTPEmailProvider(
        host="smtp.gmail.com",
        port=587,
        username="rodion.gorshkov.456@gmail.com",
        password="aubr ugra owfq aeak",
        from_email="rodion.gorshkov.456@gmail.com",
    )

def get_publisher():
    return publisher


def get_email_service(
    provider: EmailProvider = Depends(get_email_provider),
    publisher: RabbitPublisher = Depends(get_publisher)
) -> EmailService:
    return EmailService(provider, publisher)

