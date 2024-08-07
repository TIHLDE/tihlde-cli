import requests

from pydantic import ValidationError
from typing import Optional

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.api.users.user import User
from tihlde.utils import set_auth


class UserAllowPhotoResponse(Response):
    users: Optional[list[User]] = None


def get_url(page: int, event_id: str) -> str:
    return f"{URLS.EVENTS.value}/{event_id}/registrations/?&is_on_wait=false&page={page}"


def add_users(results: dict, users: list[User]):
    for reg in results:
        if reg["allow_photo"]:
            continue
        user = reg["user_info"]
        users.append(User(**user))


def allowPhotoByEvent(event_id: str) -> UserAllowPhotoResponse:
    """
    Sends a GET request to Lepton to get all users registered to an event that don't allow being photographed.
    """
    try:
        url = get_url(1, event_id)
        headers: dict = {}

        set_auth(headers)

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()

        users: list[User] = []
        add_users(data["results"], users)

        while data["next"]:
            add_users(data["results"], users)
            url = get_url(data["next"], event_id)
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
        
        user_response = UserAllowPhotoResponse(users=users)
        user_response.type = ResponseType.SUCCESS.value

        return user_response
    except requests.RequestException as e:
        try:
            json = e.response.json()
            if "detail" in json:
                return UserAllowPhotoResponse(
                    detail=json["detail"]
                )
            return UserAllowPhotoResponse(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return UserAllowPhotoResponse(
                detail=f"Network error: {e}"
            )
    except ValidationError as e:
        return UserAllowPhotoResponse(
            detail=f"Validation error: {e}"
        )