from pydantic import BaseModel



class UserCredentialsModel(BaseModel):
    login: str
    password: str



