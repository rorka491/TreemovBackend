from app.repositories.tortoise import ProfileRepository
from app.services.base import BaseService
from app.models.profile import Profile
from shared.exceptions import ProfileAlreadyExists, ObjectNotFound


class ProfileService(BaseService[ProfileRepository]):
    repo_cls = ProfileRepository


    async def get_roles(self, profile_id: int) -> list[str]:
        profile_roles = await self.repo.get_with_roles(profile_id=profile_id)
        return [obj.role for obj in profile_roles]







