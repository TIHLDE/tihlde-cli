import requests

from pydantic import ValidationError
from typing import Optional

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.api.models import Registration
from tihlde.utils import set_auth


class ListRegstrationsResponse(Response):
    registrations: Optional[list[Registration]] = None


def get_url(page: int, event_id: str) -> str:
    return f"{URLS.EVENTS.value}/{event_id}/registrations/?page={page}&is_on_wait=false"


def listRegistrations(event_id: str) -> ListRegstrationsResponse:
    """
    Sends a GET request to Lepton to get all registrations for an event.
    """
    try:
        url = get_url(1, event_id)

        headers: dict = {}
        set_auth(headers)

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()

        registrations: list[Registration] = []
        
        while data["next"]:
            for registration in data["results"]:
                registrations.append(Registration(**registration))
            url = get_url(data["next"], event_id)
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
        
        if not data["next"]:
            for registration in data["results"]:
                registrations.append(Registration(**registration))

        registrations_response = ListRegstrationsResponse(registrations=registrations)
        registrations_response.type = ResponseType.SUCCESS.value

        return registrations_response
    except requests.RequestException as e:
        try:
            json = e.response.json()
            if "detail" in json:
                return ListRegstrationsResponse(
                    detail=json["detail"]
                )
            return ListRegstrationsResponse(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return ListRegstrationsResponse(
                detail=f"Network error: {e}"
            )
    except ValidationError as e:
        return ListRegstrationsResponse(
            detail=f"Validation error: {e}"
        )

    