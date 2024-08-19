import os

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from tihlde.settings import GOOGLE_CREDENTIALS
from tihlde.models import DriveFolder


def list_drive_folders() -> list[DriveFolder]:
    service = build("drive", "v3", credentials=GOOGLE_CREDENTIALS)

    query = "mimeType='application/vnd.google-apps.folder' and trashed=false"

    results = service.files().list(q=query, pageSize=100, fields="nextPageToken, files(id, name)").execute()

    folders = results.get("files", [])

    return [
        DriveFolder(id=folder["id"], name=folder["name"])
        for folder in folders
    ]


def upload_file(file: str, folder_id: str):
    service = build("drive", "v3", credentials=GOOGLE_CREDENTIALS)

    file_metadata = {
        "name": os.path.basename(file),
        "parents": [folder_id],
        "mimeType": "application/vnd.google-apps.document"
    }
    media = MediaFileUpload(file, mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    service.files().create(body=file_metadata, media_body=media).execute()