from selenium.webdriver.common.by import By

from Utility.action_page import ActionItems


class LogInPage(ActionItems):
    username_locator = (By.NAME, "username")
    password_locator = (By.NAME, "password")
    signIn_hover = (By.LINK_TEXT, "Hello, sign in")
    click_login_locator = ''

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.do_click(self.signIn_hover)
        self.g
        self.do_send_keys(self.username_locator, username)
        self.do_send_keys(self.username_locator, password)
        self.do_click(self.click_login_locator)
