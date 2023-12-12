import pytest


def test_case1():
    print("Hello Moto!")


def test_case2():
    print("Hello Viva!")


def test_case_sanity():
    print("test_demo1_sanity")


def test_case_regression():
    print("test_demo1_regression")


@pytest.mark.smoke
def test_case_regression_smoke():
    print("test_demo1_regression_smoke")
