from typing import Callable         
from fastapi import Request
from jose import jwt, JWTError
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware



# class TenantMiddleware(BaseHTTPMiddleware):

#     async def dispatch(
#             self, 
#             request: Request, 
#             call_next: Callable[[Request], Response]
#         ) -> Response:
#         token = request.headers.get("Authorization")
#         tenant = None

#         if token and token.startswith("Bearer "):
#             try: 
#                 payload = jwt.decode(token[7:], SECRET_KEY, algorithms=[ALGORITHM])
#                 tenant = payload.get("tenant", tenant)
#             except JWTError:
#                 tenant = None

#         request.state.organization = tenant
#         response = await call_next(request)
#         return response
