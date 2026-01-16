from pydantic import BaseModel, EmailStr



class ProfileCreate(BaseModel):
    name: str
    surname: str
    pathronamic: str 

class ProfileRead(BaseModel):
    id: int
    user_id: int
    name: str
    surname: str
    pathronamic: str 

class ProfileCreateInternal(BaseModel):
    user_id: int
    role_id: int

