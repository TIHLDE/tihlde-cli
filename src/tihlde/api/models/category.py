from pydantic import BaseModel


class Category(BaseModel):
    id: int
    text: str