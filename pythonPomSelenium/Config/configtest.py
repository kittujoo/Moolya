import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class", params=["Chrome"])
def setup(request):
    global driver

    def get_connection(browser_type):
        try:
            service_object = Service()
            if browser_type == "Chrome":
                return webdriver.Chrome(service=service_object)

            elif browser_type == "Firefox":
                return webdriver.Firefox(service=service_object)

            elif browser_type == "Edge":
                return webdriver.Edge(service=service_object)

            else:
                print("Browser type is incorrect / please check")
        except Exception as e:
            print("Browser not found : ", e)
            exit(0)

    driver = get_connection(request.param)
    driver.get("https://www.amazon.in/?")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
