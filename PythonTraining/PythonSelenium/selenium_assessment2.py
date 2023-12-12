from selenium import webdriver
from selenium.webdriver.support.select import Select

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def place_order(order_placed):
    try:
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)  # 'service_obj' It will update the webdriver library.
        driver.implicitly_wait(20)
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.maximize_window()
        print(driver.title)

        driver.find_element(By.XPATH, "//input[@type='search']").send_keys('ca')
        time.sleep(1)
        # """Take the length of the products"""
        driver.find_element(By.XPATH, "//button[contains(text(),'ADD TO CART')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'ADD TO CART')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'ADD TO CART')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'ADD TO CART')]").click()
        driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
        driver.implicitly_wait(20)
        total_amount = driver.find_element(By.XPATH, "//div//span[@class='totAmt']").text
        print(total_amount)

        data = driver.find_elements(By.XPATH, "//table/tbody/tr")

        # print(len(data))
        # cart_amount = driver.find_element(By.XPATH, "//div[@class='products']/table/tbody/")
        def get_item_amount(driver1):
            cart_sum = 0
            for table_row in range(1, len(data) + 1):
                cart_amount = driver1.find_element(By.XPATH,
                                                   "//div[@class='products']/table/tbody/tr[" + str(
                                                       table_row) + "]/td[5]")
                cart_sum = cart_sum + int(driver1.execute_script("return arguments[0].innerText;", cart_amount))

            return cart_sum

        items_sum = get_item_amount(driver)

        assert int(items_sum) == int(total_amount)

        driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
        # select_option = Select(driver.find_element(By.ID, "dropdown-class-example"))
        # time.sleep(1)
        # select_option.select_by_index(3)
        # time.sleep(1)
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        # time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
        time.sleep(1)
        driver.save_screenshot(order_placed + ".jpg")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    place_order("order_placed1")
