from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    image: Optional[str] = None
    gender: Optional[int] = None
    allergy: Optional[str] = None
    tool: Optional[str] = None
    number_of_strikes: Optional[int] = None