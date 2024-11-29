import pytest

def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default="https://reqres.in", help="Base URL for API tests")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("base-url")

@pytest.fixture(scope="module")
def sample_data():
    """Sample data fixture for testing."""
    return {"first_name": "Rachel", "last_name": "Howell"}