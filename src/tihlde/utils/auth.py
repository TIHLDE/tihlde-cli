from tihlde.utils import get_env_key
from tihlde.enums import Env


def set_auth(headers: dict):
    token = get_env_key(Env.TIHLDE_TOKEN.value)
    
    headers["x-csrf-token"] = token