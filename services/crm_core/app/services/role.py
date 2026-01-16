from app.services.base import BaseService
from app.repositories.tortoise import RoleRepository




class RoleService(BaseService[RoleRepository]):
    repo_cls = RoleRepository

