from app.repositories.tortoise import ProfileRepository
from app.services.base import BaseService


class ProfileService(BaseService):
    repo_cls = ProfileRepository


