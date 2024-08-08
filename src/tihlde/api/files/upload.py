import requests

from io import BufferedReader
from typing import Optional

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.utils import set_auth


class UploadResponse(Response):
    url: Optional[str] = None


def uploadFile(file: BufferedReader) -> UploadResponse:
    """
    Upload a file to Azure Blob Storage.
    """
    try:
        headers: dict = {}

        set_auth(headers)

        url = URLS.UPLOAD.value

        response = requests.post(url, headers=headers, files={"file": file})

        response.raise_for_status()

        data = response.json()

        upload_response = UploadResponse(**data)
        upload_response.type = ResponseType.SUCCESS.value

        return upload_response
    except requests.RequestException as e:
        try:
            json = e.response.json()
            if "detail" in json:
                return UploadResponse(
                    detail=json["detail"]
                )
            return UploadResponse(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return UploadResponse(
                detail=f"Network error: {e}"
            )