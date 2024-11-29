import pytest


@pytest.fixture(scope="function")
def basic_fixture():
    return "Hello, pytest!"


@pytest.fixture(scope="module")
def dependent_fixture(basic_fixture):
    return f"{basic_fixture} - This is a dependent fixture."


@pytest.fixture(params=["admin", "guest", "moderator"])
def parameterized_fixture(request):
    return request.param


def test_basic_fixture(basic_fixture):
    assert basic_fixture == "Hello, pytest!"


@pytest.fixture(scope="function")
def dependent_fixture(basic_fixture):
    return f"{basic_fixture} - This is a dependent fixture."


def test_parameterized_fixture(parameterized_fixture):
    assert parameterized_fixture in ["admin", "guest", "moderator"]