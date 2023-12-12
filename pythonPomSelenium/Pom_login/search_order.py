import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from Utility.action_page import ActionItems


class SearchProduct(ActionItems):
    retry_count = 0
    MAX_RETRIES = 3

    search_box = (By.ID, "twotabsearchtextbox")
    SEARCH_INPUT = "Samsung"
    click_search_button = (By.XPATH, "//input[@type='submit']")
    select_first_product = (By.XPATH, "(//span[@class='a-price-whole'])[1]")
    add_to_cart_locator = (By.ID, "add-to-cart-button")
    # add_to_cart_locator = (By.NAME, "submit.add-to-cart")
    # add_to_cart_locator = (By.NAME, "//*[@id='add-to-cart-button']")
    confirm_add_to_cart_locator = (By.XPATH, "//*[@id='attach-sidesheet-view-cart-button']/span/input")
    got_to_cart_locator = (By.ID, "nav-cart")
    product_price_xpath = (
        By.XPATH,
        "//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold']")
    total_product_price_xpath = (
        By.XPATH, "(//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap'])[1]")
    proceed_checkout_locator = (By.XPATH, "//*[@id='sc-buy-box-ptc-button']/span/input")
    email_input_locator = (By.NAME, 'email')

    def __init__(self, driver):
        super().__init__(driver)

    def get_webpage_title(self, title):
        return self.ActionItems.get_title(title)

    def search_order(self, SEARCH_INPUT):
        try:
            self.do_send_keys(self.search_box, SEARCH_INPUT)
            self.do_click(self.click_search_button)
        except TimeoutException as e:
            if self.retry_count < self.MAX_RETRIES:
                self.retry_count += 1
                self.driver.refresh()
                self.search_order(SEARCH_INPUT)
            else:
                self.MAX_RETRIES = 3
                print(f"Maximum retries ({self.MAX_RETRIES}) reached. Exiting.")

    def select_order(self):
        self.do_click(self.select_first_product)

    def go_to_next_page(self):
        all_windows = self.driver.window_handles
        # current_window = self.driver.current_window_handle
        # print(current_window)
        # print(all_windows)
        self.get_next_window(all_windows[1])

    def add_order_item_to_cart(self):
        try:
            self.scroll_to_element(self.add_to_cart_locator)
            self.do_click(self.add_to_cart_locator)
            self.do_click(self.confirm_add_to_cart_locator)
        except TimeoutException as e:
            if self.retry_count < self.MAX_RETRIES:
                self.retry_count += 1
                self.driver.refresh()
                self.add_order_item_to_cart()
            else:
                self.MAX_RETRIES = 3
                print(f"Maximum retries ({self.MAX_RETRIES}) reached. Exiting.")

    def go_to_cart(self):
        self.do_click(self.got_to_cart_locator)

    def go_to_search_order(self, SEARCH_INPUT):
        all_windows = self.driver.window_handles
        current_window = self.driver.current_window_handle
        print(current_window)
        print(all_windows)
        self.get_next_window(all_windows[0])
        self.do_send_keys(self.search_box, SEARCH_INPUT)
        self.do_click(self.click_search_button)

    def price_validation_total_vs_item(self):
        product_price = self.get_text(self.product_price_xpath)
        total_cart_price = self.get_text(self.total_product_price_xpath)
        return total_cart_price, product_price

    def order_placement(self):
        self.do_click(self.proceed_checkout_locator)
        self.take_screenshot(self.email_input_locator, "login_page")
        time.sleep(5)
