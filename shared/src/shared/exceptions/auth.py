from fastapi import HTTPException, status



AuthContextMissing = HTTPException(status_code=401, detail="Auth context missing")
InvalidUserCredentials = HTTPException(status_code=401, detail="Invalid credentials")
InvalidTokenException = HTTPException(status_code=401, detail="Invalid token")
TokenBlackListedException = HTTPException(status_code=401, detail="Refresh token is blacklisted")
JtiNotProvided = HTTPException(status_code=401, detail="Jti not excpired")
UserIsNotActive = HTTPException(status_code=401, detail="User is not active")

PublicKeyNotProvided = HTTPException(
    status_code=503,
    detail="Public key is not available"
)
