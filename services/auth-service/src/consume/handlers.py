from src.services.user import UserService
from shared.payload import EmailVerifiedPayload
from shared.enums.queue import QueueEnum
from libs.logger import logger, RESET, GREEN
from src.services import user_service


async def email_verifed_register_handler(
    payload: EmailVerifiedPayload,
):
    logger.info(f"{GREEN}{payload}{RESET}")
    await user_service.activate_user(email=payload.email)

