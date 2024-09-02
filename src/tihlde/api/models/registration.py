from pydantic import BaseModel
from typing import Optional

from tihlde.api.users.user import User


class Registration(BaseModel):
    allow_photo: bool = False
    created_at: Optional[str] = None
    created_by_admin: bool = False
    has_paid_order: bool = False
    is_on_wait: bool = False
    payment_expiredate: Optional[str] = None
    wait_queue_number: Optional[int] = None
    user_info: Optional[User] = None