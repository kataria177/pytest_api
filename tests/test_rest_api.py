
import pytest
from pages.api_client import APIClient
from utils.config import MOCK_POST_ENDPOINT, MOCK_GET_ENDPOINT
from utils.report import generate_report


@pytest.fixture
def api_client():
    """Fixture to initialize API client."""
    return APIClient()

@pytest.mark.smoke
def test_post_and_validate(api_client):
    """Test to send a POST request and validate the data with a GET request."""
    # Payload for POST request
    post_payload = {
        "name": "Rachel",
        "job": "leader",
        "id": "12"
    }

    # Step 1: Send POST request
    response_post = api_client.post_data("api/users", post_payload)
    assert response_post is not None, "POST request returned None"
    assert response_post.status_code == 201, "POST request failed"

    # Extract data from POST response
    posted_data = response_post.json()
    assert "id" in posted_data, "POST response missing 'id'"
    assert "createdAt" in posted_data, "POST response missing 'createdAt'"
    user_id = posted_data["id"]  # Save the generated user ID
    print(f"User created with ID: {user_id}")

    # Step 2: Send GET request to validate the posted user
    response_get = api_client.get_data(f"api/users/{user_id}")
    assert response_get is not None, "GET request returned None"
    assert response_get.status_code == 200, "GET request failed"

    # Extract data from GET response
    fetched_data = response_get.json()
    assert "data" in fetched_data, "GET response missing 'data'"
    user_data = fetched_data["data"]

    # Validate GET response matches the POST data
    assert user_data["id"] == int(user_id), "User ID mismatch"
    assert user_data["first_name"] == post_payload["name"], "First name mismatch"
    print("GET response validated successfully.")

    # Log the GET response for reference
    print("GET response data:", user_data)

    # Validate GET response matches POST data
    get_data = response_get.json().get("args")
    # print(f'response GET {user_data} ----- {post_payload}')
    # assert user_data == post_payload, "GET data does not match POST data"

    # Generate and log report
    report = generate_report(response_post, response_get, get_data == post_payload)
    print(report)
