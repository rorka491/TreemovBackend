from fastapi import APIRouter, Depends
from app.depends.profile import get_profile_service
from app.depends.auth import get_auth_context
from app.services.profile import ProfileService
from app.filters import BaseModelFilter
from shared.schemas.profile import ProfileRead, ProfileCreate, ProfileCreateInternal
from shared.dataclass.auth import AuthContext



router = APIRouter(prefix='/profiles', tags=['profile'])


@router.get('/me', response_model=ProfileRead)
async def get_my_profile(
    user: AuthContext = Depends(get_auth_context),
    profile_service: ProfileService = Depends(get_profile_service)
):
    return await profile_service.get_by_id(id=user.user_id)


@router.get('/me', response_model=ProfileRead)
async def create_my_profile(
    profile_data: ProfileCreate,
    user: AuthContext = Depends(get_auth_context),
    profile_service: ProfileService = Depends(get_profile_service)
):
    profile_data_internal = ProfileCreateInternal(
        user_id=user.user_id,
        **profile_data.model_dump()
    )
    return await profile_service.create(profile_data_internal, profile_exists=user.profile_exists)


@router.get('', response_model=list[ProfileRead])
async def get_profiles(
    profile_service: ProfileService = Depends(get_profile_service)
):
    return await profile_service.get_all()

