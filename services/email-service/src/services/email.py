import random
from datetime import datetime, timedelta, UTC
from tortoise.exceptions import DoesNotExist

from src.models.email import EmailCode
from src.core.config import hasher
from src.email_provider import EmailProvider


from shared.schemas.email import VerifyCodeSchema, SendCodeSchema
from shared.payload import EmailVerifiedPayload
from shared.enums.queue import QueueEnum
from shared.enums.email import EmailCodePurpose, PurposeQueueMapping
from shared.exceptions.queue import QueueNotFound
from libs.rabbit.publisher import RabbitPublisher





class EmailService:
    def __init__(self, provider: EmailProvider, producer: RabbitPublisher):
        self.provider = provider
        self.producer = producer
        
    async def create_code(
        self,
        email: str,
        purpose: EmailCodePurpose,
        code: str
    ) -> EmailCode:
        await EmailCode.filter(
            email=email,
            purpose=purpose,
            is_used=False
        ).update(is_used=True)

        expires = datetime.now(UTC) + timedelta(minutes=10)

        obj = await EmailCode.create(
            email=email, 
            code=hasher.hash(code), 
            purpose=purpose, 
            expires_at=expires
        )
        return obj
    

    async def send_code(self, payload: SendCodeSchema) -> EmailCode:
        
        code = f"{random.randint(100000, 999999)}"
        await self.create_code(email=payload.email, code=code, purpose=payload.purpose)
        try:
            await self.provider.send(
                to=payload.email,
                subject=payload.purpose.value,
                body=code
            )
        except Exception as e:
            raise e


    async def verify_code(self, payload: VerifyCodeSchema) -> bool:
        obj = await EmailCode.get_or_none(
            email=payload.email, 
            purpose=payload.purpose,
            is_used=False
        )
        if not obj or obj.is_expired:
            return False
        
        if not hasher.verify(payload.code, obj.code):
            return False

        obj.is_used = True
        await obj.save()

        purpose = payload.purpose
        payload = EmailVerifiedPayload(
            email=payload.email,
            purpose=purpose.value
        )
        try:
            await self.producer.publish(
                payload=payload, 
                queue=PurposeQueueMapping[purpose]
            )
        except KeyError:
            raise QueueNotFound
        
        return True
    



