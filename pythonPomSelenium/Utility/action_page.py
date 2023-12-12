import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ActionItems:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).click()
        # time.sleep(2)

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        time.sleep(2)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def take_screenshot(self, locator, file_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.save_screenshot(file_name + '.png')

    def get_next_window(self, window):
        self.driver.switch_to.window(window)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

        # return self.driver.find_element(locator).text

    def scroll_to_element(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            # self.driver.execute_script("arguments[0].scrollIntoView();", locator)
        except TimeoutException:
            print("Element not found within the specified time.")
