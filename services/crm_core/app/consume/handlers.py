from shared.payload import UserCreatedPayload
from app.services.profile import ProfileService
from app.services.role import RoleService
from app.core.config import logger, RESET, GREEN
from shared.schemas.profile import ProfileCreateInternal
from app.services import profile_service, role_service


async def handle_user_created(
    payload: UserCreatedPayload,
    profile_service: ProfileService = profile_service,
    role_service: RoleService = role_service
):
    role = await role_service.get(code=payload.role)

    logger.info(f"{GREEN}{payload}{RESET}")

    profile_data = ProfileCreateInternal(
        user_id=payload.user_id, 
        role_id=role.id
    )
    
    await profile_service.create(profile_data)

    logger.warning('profile_create')

