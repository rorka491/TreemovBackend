from fastapi import HTTPException, status


QueueNotFound = HTTPException(status_code=500, detail="Queue not found")
