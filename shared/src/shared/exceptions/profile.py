from fastapi import HTTPException

ProfileNotFound = HTTPException(status_code=403, detail="Profile not found")
ProfileAlreadyExists = HTTPException(status_code=409, detail='Profile already exists')