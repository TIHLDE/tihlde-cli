from pydantic import BaseModel


class Field(BaseModel):
    id: str
    title: str
    type: str
    required: bool
    options: list[str]
    order: int


class Form(BaseModel):
    title: str
    id: str
    resource_type: str
    fields: list[Field]