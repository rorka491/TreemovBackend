from fastapi import Header, HTTPException
from app.core.config import SECRET_AGENT_KEY

def agent_required(x_api_key: str = Header(...)):
    if x_api_key != SECRET_AGENT_KEY:
        raise HTTPException(403, "Forbidden")
