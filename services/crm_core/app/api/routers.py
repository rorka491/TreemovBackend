from fastapi import APIRouter
from app.api.init_org import router as org_router
from app.api.profile import router as profile_router


router = APIRouter(prefix="/api/v1")

router.include_router(org_router)
router.include_router(profile_router)