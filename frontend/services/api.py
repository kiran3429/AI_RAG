import requests

BACKEND_URL = "http://127.0.0.1:8000"


def get_rags():
    response = requests.get(f"{BACKEND_URL}/rags")
    response.raise_for_status()
    return response.json()