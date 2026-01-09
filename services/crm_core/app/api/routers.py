from fastapi import APIRouter
from app.api.init_org import router as org_router



router = APIRouter(prefix="/api/v1")

router.include_router(org_router)

