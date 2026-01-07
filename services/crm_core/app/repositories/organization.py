from app.models.base import BaseModelPK
from app.models.organization import Organization
from app.repositories.base import TortoiseRepository


class OrganizationRepository(TortoiseRepository):
    model: BaseModelPK = Organization