from pydantic import BaseModel, Field


class BaseModelRead(BaseModel):
    id: int

    model_config = {"from_attributes": True}


class BaseModelCreate(BaseModel): ...


class BaseModelUpdate(BaseModel): ...
