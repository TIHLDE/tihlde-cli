import requests

from pydantic import ValidationError
from typing import Optional

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.api.models.form import Form
from tihlde.utils import set_auth


class FormResponse(Response):
    forms: Optional[list[Form]] = None


def getGroupForms(group: str) -> FormResponse:
    """
    Sends a GET request to Lepton to get all forms of a group.
    """
    try:
        url = f"{URLS.GROUPS.value}{group}/forms/"

        headers: dict = {}
        set_auth(headers)

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()

        forms: list[Form] = []
        for form in data:
            forms.append(Form(**form))

        forms_response = FormResponse(forms=forms)
        forms_response.type = ResponseType.SUCCESS.value

        return forms_response
    except requests.RequestException as e:
        try:
            json = e.response.json()
            if "detail" in json:
                return FormResponse(
                    detail=json["detail"]
                )
            return FormResponse(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return FormResponse(
                detail=f"Network error: {e}"
            )
    except ValidationError as e:
        return FormResponse(
            detail=f"Validation error: {e}"
        )