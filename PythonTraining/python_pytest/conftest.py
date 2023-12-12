import pytest


@pytest.fixture(scope='class')
def setup():
    print("Driver.Open : Start the browser and application")
    yield
    print("Driver.Close : Close the browser and application")


@pytest.fixture(params=['chrome', 'firefox'])
def data(request):
    return request.param


@pytest.fixture(scope='class')
def name():
    return ['Moto', 'Viva', 'Oppo']


def names():
    return ['Moto', 'Viva', 'Oppo']


@pytest.fixture(params=names())
def return_names(request):
    return request.param
