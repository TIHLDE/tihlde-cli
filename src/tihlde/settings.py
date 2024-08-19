from google.oauth2 import service_account


# User settings
USER_DIR = "user"
USER_DOWNLOAD_DIR = f"{USER_DIR}/download"
USER_UPLOAD_DIR = f"{USER_DIR}/upload"
USER_TEMP_DIR = f"{USER_DIR}/temp"
USER_OWN_FILES = f"{USER_DIR}/my_files"

# Google settings
GOOGLE_CREDENTIALS = "src/tihlde/auth/google_credentials.json"
GOOGLE_SCOPES = ["https://www.googleapis.com/auth/drive"]
GOOGLE_CREDENTIALS = service_account.Credentials.from_service_account_file(
    GOOGLE_CREDENTIALS,
    scopes=GOOGLE_SCOPES
)