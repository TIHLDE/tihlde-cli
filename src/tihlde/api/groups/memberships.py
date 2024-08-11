import requests

from pydantic import ValidationError
from typing import Optional

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.api.users.user import User
from tihlde.utils import set_auth


class MembershipResponse(Response):
    memberships: Optional[list[User]] = None


def getMemberships(group: str) -> MembershipResponse:
    """
    Sends a GET request to Lepton to get all members of a group.
    """
    try:
        url = f"{URLS.GROUPS.value}{group}/memberships/?onlyMembers=true"

        headers: dict = {}
        set_auth(headers)

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()

        memberships: list[User] = []
        for user_rec in data["results"]:
            user = user_rec["user"]
            memberships.append(User(**user, group=group))

        memberships_response = MembershipResponse(memberships=memberships)
        memberships_response.type = ResponseType.SUCCESS.value

        return memberships_response
    except requests.RequestException as e:
        try:
            json = e.response.json()
            if "detail" in json:
                return MembershipResponse(
                    detail=json["detail"]
                )
            return MembershipResponse(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return MembershipResponse(
                detail=f"Network error: {e}"
            )
    except ValidationError as e:
        return MembershipResponse(
            detail=f"Validation error: {e}"
        )