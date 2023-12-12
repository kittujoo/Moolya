# conftest.py

import logging
import pytest


@pytest.fixture(scope='session', autouse=True)
def setup_logging(request):
    global logger
    # Create a custom logger
    logger = logging.getLogger('test_suite_logger')
    logger.setLevel(logging.INFO)

    # Create a file handler and set level to INFO
    fh = logging.FileHandler('test_suite_log1.txt')
    fh.setLevel(logging.INFO)

    # Create a console handler and set level to INFO
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    yield logger
    # def teardown():
    logging.shutdown()

    # request.addfinalizer(teardown)

    # return logger


def log_test(func):
    def wrapper(*args, **kwargs):
        # logger = setup_logging
        logger.info(f"Running test: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Test {func.__name__} completed.")
        return result

    return wrapper
