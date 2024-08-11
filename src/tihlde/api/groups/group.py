from pydantic import BaseModel
from typing import Optional

from tihlde.api.users.user import User


class Group(BaseModel):
    name: str
    slug: str
    type: str
    leader: Optional[User] = None
