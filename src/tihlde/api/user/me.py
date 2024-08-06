import requests

from typing import Optional

from tihlde.enums import URLS, Env
from tihlde.api.response import Response
from tihlde.utils import get_env_key


class MeResponse(Response):
    user_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


def getMe() -> MeResponse:
    """
    Sends a GET request to Lepton to get information about the user.
    """
    try:
        token = get_env_key(Env.TIHLDE_TOKEN.value)
        if not token:
            return MeResponse(
                detail="You are not logged in"
            )

        headers = {
            "x-csrf-token": token
        }

        url = URLS.ME.value

        response = requests.get(url, headers=headers)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse response JSON
        data = response.json()

        # Validate and parse the response using Pydantic
        me_response = MeResponse(**data)
        me_response.type = "success"

        return me_response
    except requests.RequestException as e:
        # Handle network-related errors
        try:
            json = e.response.json()
            if "detail" in json:
                return MeResponse(
                    detail=json["detail"]
                )
            return MeResponse(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return MeResponse(
                detail=f"Network error: {e}"
            )
