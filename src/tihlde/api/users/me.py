import requests

from typing import Optional
from pydantic import ValidationError

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.utils import set_auth


class MeResponse(Response):
    user_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


def getMe() -> MeResponse:
    """
    Sends a GET request to Lepton to get information about the user.
    """
    try:
        headers: dict = {}

        set_auth(headers)

        url = URLS.ME.value

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()

        me_response = MeResponse(**data)
        me_response.type = ResponseType.SUCCESS.value

        return me_response
    except requests.RequestException as e:
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
    except ValidationError as e:
        return MeResponse(
            detail=f"Validation error: {e}"
        )
