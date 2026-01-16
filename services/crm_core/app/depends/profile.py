from fastapi import Depends
from app.repositories.tortoise import ProfileRepository
from app.services.profile import ProfileService


def get_profile_service() -> ProfileService:
    return ProfileService()