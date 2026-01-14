from pydantic import BaseModel
from shared.schemas.profile import ProfileCreate
from shared.schemas.user import UserCreate




class RegisterRequest(BaseModel):
    user: UserCreate
    profile: ProfileCreate
