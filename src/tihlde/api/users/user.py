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
    group: Optional[str] = None

    def __hash__(self):
        return hash((self.user_id, self.email))

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return (self.user_id, self.email) == (other.user_id, other.email)