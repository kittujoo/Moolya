import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Config.configtest import setup
from Pom_login.search_order import SearchProduct


@pytest.mark.usefixtures("setup")
class Test_Login:
    SEARCH_ITEM = "Samsung"

    def test_login_screenshot(self, setup):
        pass




