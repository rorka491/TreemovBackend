from fastapi import APIRouter, Response
from fastapi.responses import FileResponse
from src.api.auth import router as auth_router
from src.api.user import router as user_router
from src.core.config import PUBLIC_KEY_PATH
from src.produce.producers import producer

router = APIRouter(prefix='/api/v1')

router.include_router(auth_router)
router.include_router(user_router)


@router.get('/ping')
async def ping():
    return {"status": "ok"}


@router.get("/public_key", response_class=FileResponse)
async def get_public_key():
    if PUBLIC_KEY_PATH.exists():
        return FileResponse(PUBLIC_KEY_PATH, media_type="application/octet-stream", filename="public.pem")
    return {"error": "File not found"}


@router.post('/test_message')
async def test_message():
    await producer.test_publish()
    return {'detail': 'success'}

