import pytest


@pytest.fixture()
def setup():
    print("Driver.Open : Start the browser and application")
    yield
    print("Driver.Close : Close the browser and application")


def test_case6(setup):
    print("This is first test function")


def test_case7(setup):
    print("This is second test function")
