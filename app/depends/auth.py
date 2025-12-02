from app.services.auth import AuthService
from app.repositories.user import UserRepository

async def get_auth_service():
    return AuthService(UserRepository())
