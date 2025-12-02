from pydantic import Field
from app.schemas.base import BaseModelCreate, BaseModelRead


class OrganizationModelCreate(BaseModelCreate):
    title: str

class OrganizationModelRead(BaseModelRead):
    title: str = Field(..., read_only=True)
