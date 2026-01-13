from fastapi import APIRouter, Depends
from app.depends import get_profile_service
from app.services.profile import ProfileService
from app.filters import BaseModelFilter
from shared.schemas.profile import ProfileRead


router = APIRouter(prefix='/profiles', tags=['profile'])


@router.get('', response_model=list[ProfileRead])
async def get_profiles(
    profile_service: ProfileService = Depends(get_profile_service)
):
    profiles = await profile_service.get_all()
    return profiles