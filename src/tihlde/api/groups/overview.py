import requests

from pydantic import ValidationError
from typing import Optional

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.api.groups.group import Group
from tihlde.utils import set_auth


class GroupOverviewResponse(Response):
    groups: Optional[list[Group]] = None


def getGroups() -> GroupOverviewResponse:
    """
    Sends a GET request to Lepton to get all groups.
    """
    try:
        url = URLS.GROUPS_OVERVIEW.value

        headers: dict = {}
        set_auth(headers)

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()

        groups_response = GroupOverviewResponse(
            groups=[Group(**group) for group in data]
        )

        groups_response.type = ResponseType.SUCCESS.value

        return groups_response
    except requests.RequestException as e:
        try:
            json = e.response.json()
            if "detail" in json:
                return GroupOverviewResponse(
                    detail=json["detail"]
                )
            return GroupOverviewResponse(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return GroupOverviewResponse(
                detail=f"Network error: {e}"
            )
    except ValidationError as e:
        return GroupOverviewResponse(
            detail=f"Validation error: {e}"
        )