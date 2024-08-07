import requests

from pydantic import ValidationError
from typing import Optional

from tihlde.enums import URLS
from tihlde.api.response import Response


class AuthResponse(Response):
    token: Optional[str] = None


def authenticate(username: str, password: str) -> AuthResponse:
    """
    Sends a POST request to Lepton with the provided username and password.
    """
    try:
        url = URLS.AUTH.value
        data = {'user_id': username, 'password': password}

        response = requests.post(url, data=data)
        
        response.raise_for_status() 

        data = response.json()

        auth_response = AuthResponse(**data)

        if auth_response.token:
            return AuthResponse(
                type="success",
                token=auth_response.token
            )
        
        return AuthResponse(
            detail="Invalid username or password"
        )
    
    except requests.RequestException as e:
        try:
            json = e.response.json()
            if "detail" in json:
                return AuthResponse(
                    detail=json["detail"]
                )
            return AuthResponse(
                detail=f"Network error: {e}"
            )
        except ValueError:
            return AuthResponse(
                detail=f"Network error: {e}"
            )
        
    except ValidationError as e:
        return AuthResponse(
            detail=f"Invalid response structure: {e}"
        )