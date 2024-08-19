from enum import Enum

from tihlde.constants import TIHLDE_API_URL


class URLS(Enum):
    AUTH = f"{TIHLDE_API_URL}/auth/login/"
    ME = f"{TIHLDE_API_URL}/users/me/?/"
    USERS = f"{TIHLDE_API_URL}/users/"
    EVENTS = f"{TIHLDE_API_URL}/events/"
    UPLOAD = f"{TIHLDE_API_URL}/upload/"
    DELETE_FILE = f"{TIHLDE_API_URL}/delete-file/"
    GROUPS = f"{TIHLDE_API_URL}/groups/"
    GROUPS_OVERVIEW = f"{TIHLDE_API_URL}/groups?overview=true"
    FORMS = f"{TIHLDE_API_URL}/forms/"