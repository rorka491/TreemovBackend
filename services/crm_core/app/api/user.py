from fastapi import APIRouter, Depends, Request
from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.depends.user import get_user_service
from app.services.user import UserService

router = APIRouter(prefix='/users')


@router.post("/create", response_model=UserRead)
async def create_user(
    user_data: UserCreate, 
    user_service: UserService = Depends(get_user_service)
):
    user = await user_service.create_user(user_data)
    return user
