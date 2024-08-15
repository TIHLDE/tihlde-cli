from pydantic import BaseModel
from datetime import datetime

from tihlde.api.groups.group import Group
from tihlde.api.models import Category


class Event(BaseModel):
    id: int
    title: str
    start_date: datetime
    end_date: datetime
    expired: bool
    location: str
    organizer: Group
    category: Category 