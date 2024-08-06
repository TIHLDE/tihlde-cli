from enum import Enum

from tihlde.constants import TIHLDE_API_URL


class URLS(Enum):
    AUTH = f"{TIHLDE_API_URL}/auth/login/"
    ME = f"{TIHLDE_API_URL}/users/me/?/"