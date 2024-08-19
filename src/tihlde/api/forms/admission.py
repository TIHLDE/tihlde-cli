import requests

from pydantic import ValidationError
from typing import Optional

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.api.models import Admission
from tihlde.utils import set_auth


class AdmissionResponse(Response):
    admissions: Optional[list[Admission]] = None


def get_url(page: int, id: int) -> str:
    return f"{URLS.FORMS.value}{id}/submissions/?page={page}"

def getAdmissions(id: str) -> AdmissionResponse:
    """
    Sends a GET request to Lepton to get all admissions from a form.
    """
    try:
        url = get_url(1, id)

        headers: dict = {}
        set_auth(headers)

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()

        admissions: list[Admission] = []
        for admission in data["results"]:
            admissions.append(Admission(**admission))

        while data["next"]:
            for admission in data["results"]:
                admissions.append(Admission(**admission))
            url = get_url(data["next"], id)
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

        admissions_response = AdmissionResponse(admissions=admissions)
        admissions_response.type = ResponseType.SUCCESS.value

        return admissions_response
    except requests.RequestException as e:
        try:
            json = e.response.json()
            if "detail" in json:
                return AdmissionResponse(
                    detail=json["detail"]
                )
            return AdmissionResponse(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return AdmissionResponse(
                detail=f"Network error: {e}"
            )
    except ValidationError as e:
        return AdmissionResponse(
            detail=f"Validation error: {e}"
        )