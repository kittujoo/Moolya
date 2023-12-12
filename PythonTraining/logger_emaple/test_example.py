from logger_emaple.conftest import log_test

@log_test
def test_1():
    print("Test1")
    assert 1 == 2


@log_test
def test_2():
    print("Test2")


@log_test
def test_3():
    print("Test3")