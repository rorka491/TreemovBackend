from fastapi import Depends, HTTPException, Request


def tenant_required(request: Request):
    if request.state.organization is None:
        raise HTTPException(status_code=403, detail="Access denied: tenant is required")
