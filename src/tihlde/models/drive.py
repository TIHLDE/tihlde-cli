from pydantic import BaseModel


class DriveFolder(BaseModel):
    id: str
    name: str