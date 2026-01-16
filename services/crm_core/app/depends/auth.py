from fastapi import Header, HTTPException
from app.core.config import token_service
from app.depends.profile import get_profile_service
from app.services.profile import ProfileService
from shared.dataclass.auth import AuthContext
from shared.exceptions import AuthContextMissing, ProfileNotFound
from shared.enums.auth import UserRole




async def get_token_service():
    return token_service


async def get_auth_context(
    x_user_id: str = Header(...),
    x_user_role: str = Header(...),
) -> AuthContext:
    if not x_user_id:
        raise AuthContextMissing
    profile_service: ProfileService = get_profile_service()

    user_role = UserRole(x_user_role)
    profile = await profile_service.repo.get(id=x_user_id)
    
    if profile:
        profile_roles = await profile_service.get_roles(profile_id=profile.id)
        profile_exists = True
    else:
        profile_roles = []
        profile_exists = False

    
    return AuthContext(
        user_id=x_user_id, 
        user_role=user_role, 
        profile_roles=profile_roles, 
        profile_exists=profile_exists
    )