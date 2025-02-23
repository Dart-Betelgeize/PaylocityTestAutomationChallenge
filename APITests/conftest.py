import pytest
from api_clients.api_client import APIClient
from api_clients.auth_client import AuthClient
from utils.env_data import BASE_API_URL

@pytest.fixture(scope="module")
def auth_token():
    # Initialize AuthClient with necessary details
    auth_client = AuthClient()
    return auth_client.get_token()

@pytest.fixture(scope="module")
def api_client(auth_token):
    # Initialize the APIClient with the base URL and token
    return APIClient(base_url=BASE_API_URL, token=auth_token)
