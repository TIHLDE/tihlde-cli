import requests

from tihlde.enums import URLS, ResponseType
from tihlde.api.response import Response
from tihlde.utils import set_auth
from tihlde.db import get_file


def extract_file_info_from_url(url: str) -> tuple[str, str]:
    """
    Extract container name and blob name from the URL.
    """
    parts = url.split("/")
    return parts[-2], parts[-1]


def deleteFile(file_id: str) -> Response:
    """
    Deletes a file from Azure Blob Storage.
    """
    try:
        headers: dict = {}

        set_auth(headers)

        file = get_file(file_id)

        if not file:
            return Response("File not found")

        container_name, blob_name = extract_file_info_from_url(file.url)

        url = f"{URLS.DELETE_FILE.value}{container_name}/{blob_name}/"

        response = requests.delete(url, headers=headers)

        response.raise_for_status()
        
        return Response(type=ResponseType.SUCCESS)
    
    except requests.RequestException as e:
        try:
            json = e.response.json()
            if "detail" in json:
                return Response(
                    detail=json["detail"]
                )
            return Response(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return Response(
                detail=f"Network error: {e}"
            )