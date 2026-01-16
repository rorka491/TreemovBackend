import httpx
# from app.core.config import BASE_URL_ACCOUNTS_SERVICE



class ExternalService:
    BASE_URL = "http://other-service"

    async def get_user(self, user_id: int):
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{self.BASE_URL}/users/{user_id}")
            r.raise_for_status()
            return r.json()


external_service = ExternalService()
