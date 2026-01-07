from fastapi import APIRouter, Request, Depends 
from app.schemas.organization import OrganizationModelCreate, OrganizationModelRead
from app.depends.agent import agent_required
from app.models.organization import Organization

router = APIRouter(prefix='/organizations')

@router.post('/init', response_model=OrganizationModelRead)
async def init_organization_schema(
    request: Request, 
    org_data: OrganizationModelCreate, 
    _=Depends(agent_required)
):
    
    return OrganizationModelRead.model_validate(org)


