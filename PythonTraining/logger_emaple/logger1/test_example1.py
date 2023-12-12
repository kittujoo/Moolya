# test_example1.py

from conftest import setup_logging

# logger = setup_logging

def log_test(func):
    def wrapper(*args, **kwargs):
        logger = setup_logging
        logger.info(f"Running test: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Test {func.__name__} completed.")
        return result
    return wrapper

@log_test
def test_example1():
    assert 1 == 1
