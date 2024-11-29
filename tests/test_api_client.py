import pytest
from pages.api_client import APIClient

@pytest.fixture
def api_client():
    """Fixture to initialize API client."""
    return APIClient()


def test_get_users(api_client):
    """Tests the GET endpoint of the API."""
    response = api_client.get_data("api/users/12")
    assert response.status_code == 200
    data = response.json()
    print(f'data from get - {data}')
    assert "data" in data
    assert len(data["data"]) > 0


def test_create_user(api_client, sample_data):
    """Tests the POST endpoint of the API."""
    response = api_client.post_data("api/users", sample_data)
    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data
    assert "createdAt" in response_data