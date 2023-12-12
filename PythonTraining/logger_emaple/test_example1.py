# test_example1.py

from conftest import log_test

@log_test
def test_example1():
    assert 1 == 1
