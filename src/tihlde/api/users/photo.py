import requests

from pydantic import ValidationError
from typing import Optional

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.api.users.user import User
from tihlde.utils import set_auth


class UserAllowPhotoResponse(Response):
    users: Optional[list[User]] = None


def get_url(page: int) -> str:
    return f"{URLS.USERS.value}?has_allowed_photo=false&page={page}"


def allowPhoto() -> UserAllowPhotoResponse:
    """
    Sends a GET request to Lepton to get all users that don't allow being photographed.
    """
    try:
        url = get_url(1)
        headers: dict = {}

        set_auth(headers)

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()

        users: list[User] = []
        for user in data["results"]:
            users.append(User(**user))

        while data["next"]:
            for user in data["results"]:
                users.append(User(**user))
            url = get_url(data["next"])
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