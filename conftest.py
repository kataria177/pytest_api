import pytest
def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default="https://httpbin.org", help="Base URL for API tests")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("base-url")
