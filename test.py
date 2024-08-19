from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload
import io
from googleapiclient.errors import HttpError

scope = ['https://www.googleapis.com/auth/drive']
service_account_json_key = 'google/credentials.json'
credentials = service_account.Credentials.from_service_account_file(
                              filename=service_account_json_key, 
                              scopes=scope)

service = build("drive", "v3", credentials=credentials)

# Call the Drive v3 API
folder_id = "1LbfMFfpNnZvHFDVIRsnkXy9DOBeCsfwb"
query = f"'{folder_id}' in parents and trashed=false"

results = (
    service.files()
    .list(pageSize=10, fields="nextPageToken, files(id, name)", q=query)
    .execute()
)
items = results.get("files", [])

for item in items:
    print(item)