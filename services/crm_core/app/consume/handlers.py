from shared.payload import UserCreatedPayload
from app.services.profile import ProfileService
from app.core.config import logger, RESET, GREEN
from app.depends import get_profile_service



async def handle_user_created(payload: UserCreatedPayload):
    profile_service = ProfileService()
    logger.info(f"{GREEN}{payload}{RESET}")
    await profile_service.create(payload)
    logger.warning('profile_create')

