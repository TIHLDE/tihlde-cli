from pydantic import BaseModel

from tihlde.api.users.user import User


class Field(BaseModel):
    id: str


class Answer(BaseModel):
    answer_text: str
    id: str
    selected_options: list[str]
    field: Field


class Admission(BaseModel):
    answers: list[Answer]
    user: User