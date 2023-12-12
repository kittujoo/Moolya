import pytest


@pytest.mark.skip("Name Incorrect")
def test_case3():
    name = 'Hi'
    assert name == 'Hello'


def test_case4():
    name = 'Hello'
    assert name == 'Hello'


@pytest.mark.smoke("Name Incorrect")
@pytest.mark.xfail
def test_case3():
    name = 'Hi'
    assert name == 'Hello'


def test_case_sanity():
    print("test_demo2_sanity")


def test_case_regression():
    print("test_demo2_regression")


@pytest.mark.smoke
def test_case_regression_smoke():
    print("test_demo2_regression_smoke")
