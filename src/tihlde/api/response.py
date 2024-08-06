from pydantic import BaseModel, validator

from typing import Optional


class Response(BaseModel):
    type: str = "error"
    detail: Optional[str] = None

    @validator("type")
    def validate_type(cls, v):
        if v not in ["success", "error"]:
            raise ValueError("type must be either 'success' or 'error'")
        return v