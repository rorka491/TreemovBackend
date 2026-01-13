from fastapi import HTTPException, status



UserAlreadyExistsException = HTTPException(status_code=400, detail="User already exists")
UserNotFoundNotAuthException = HTTPException(status_code=401, detail="User not found")

UniqueFieldRequiredException = HTTPException(
    status_code=400,
    detail="Field must be unique"
)

ObjectNotFound = HTTPException(
    status_code=404,
    detail="Object not found"
)
