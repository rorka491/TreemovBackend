from app.repositories.user import UserRepository
from app.services.user import UserService



async def get_user_service():
    return UserService(UserRepository())
