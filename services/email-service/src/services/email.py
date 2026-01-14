import random
from datetime import datetime, timedelta, UTC
from tortoise.exceptions import DoesNotExist
from src.enums import CodePurpose
from src.models.email import EmailCode
from src.core.config import hasher
from src.email_provider import EmailProvider


from shared.schemas.email import SendCodeSchema
from shared.schemas.email import VerifyCodeSchema, SendCodeSchema
from shared.payload import EmailVerifiedPayload
from shared.enums.queue import QueueEnum
from libs.rabbit.publisher import RabbitPublisher




class EmailService:
    def __init__(self, provider: EmailProvider, producer: RabbitPublisher):
        self.provider = provider
        self.producer = producer
        
    async def create_code(
        self,
        email: str,
        purpose: CodePurpose,
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
        try:
            obj = await EmailCode.get(
                email=payload.email, 
                purpose=payload.purpose,
                is_used=False
            )

        except DoesNotExist:
            return False

        if obj.is_expired:
            return False
        
        if not hasher.verify(obj.code, payload.code):
            return False

        obj.is_used = True
        payload = EmailVerifiedPayload(email = payload.email)
        self.producer.publish(payload=payload, queue=QueueEnum.EMAIL_REGISTER_VERIFIED)
        self.producer.publish(payload=payload, queue=QueueEnum.EMAIL_LOGIN_VERIFIED)
        await obj.save()
        return True
    



