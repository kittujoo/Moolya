import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service_object = Service()
driver = webdriver.Chrome(service=service_object)
LOGIN_URL = "https://www.amazon.in/"
signIn_hover = (By.LINK_TEXT, "Hello, sign in")
search_box = (By.ID, "twotabsearchtextbox")
SEARCH_INPUT = "Samsung"
driver.get(LOGIN_URL)
driver.maximize_window()


def do_click(locator):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator)).click()
    time.sleep(5)


def do_send_keys(locator, key_to_input):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(key_to_input).click()
    time.sleep(5)

do_click(signIn_hover)
# do_click(search_box)
do_send_keys(search_box, SEARCH_INPUT)
