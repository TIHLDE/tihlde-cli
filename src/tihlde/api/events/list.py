import requests

from pydantic import ValidationError
from typing import Optional

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.utils import set_auth
from tihlde.api.models import Event


class ListEventsResponse(Response):
    events: Optional[list[Event]] = None


def create_url(page: int | None, activity: bool, expired: bool) -> str:
    url = URLS.EVENTS.value

    url += f"?page={page if page else 1}"

    if activity:
        url += "&activity=true"

    if expired:
        url += "&expired=true"

    return url


def listEvents(
    page: int | None,
    activity: bool,
    expired: bool
) -> ListEventsResponse:
    """
    Sends a GET request to Lepton to get all events.
    """
    try:
        url = create_url(page, activity, expired)

        headers: dict = {}
        set_auth(headers)

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()

        events_response = ListEventsResponse(
            events=[Event(**event) for event in data["results"]]
        )

        events_response.type = ResponseType.SUCCESS.value

        return events_response
    except requests.RequestException as e:
        try:
            json = e.response.json()
            if "detail" in json:
                return ListEventsResponse(
                    detail=json["detail"]
                )
            return ListEventsResponse(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return ListEventsResponse(
                detail=f"Network error: {e}"
            )
    except ValidationError as e:
        return ListEventsResponse(
            detail=f"Validation error: {e}"
        )