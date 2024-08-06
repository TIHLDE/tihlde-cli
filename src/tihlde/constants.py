import os

from dotenv import load_dotenv

load_dotenv()


ENV = os.getenv("ENVIRONMENT", "PROD")

TIHLDE_API_URL = "https://api.tihlde.org" if ENV == "PROD" else "http://localhost:8000"