from fastapi import APIRouter
from src.api.email import router as email_router


router = APIRouter(tags=['email'])
router.include_router(email_router)