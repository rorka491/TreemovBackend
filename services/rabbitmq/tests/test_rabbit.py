import pytest
from httpx import AsyncClient
from src.config import RABBIT_URL_TEST
from shared import EventFactory, EventType
from shared.rabbit.publisher import RabbitPublisher
from shared.rabbit.rabbit_init import EXCHANGE_NAME
from shared.contracts.payload import EmailVerifiedPayload



payload = EmailVerifiedPayload(user_id=1, email="rodion@mail.ru")

@pytest.fixture
def publisher():
    return RabbitPublisher(
        url=RABBIT_URL_TEST,
        exchange_name=EXCHANGE_NAME
    )

@pytest.mark.asyncio
async def test_rabbit_publish(publisher: RabbitPublisher):
    event = EventFactory.create(
        event_type=EventType.EMAIL_LOGIN_VERIFIED,
        payload_obj=payload
    )
    await publisher.connect()
    publisher.publish(event=event)




