from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def orange_hrm():
    try:

        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)  # 'service_obj' It will update the webdriver library.
        driver.maximize_window()

        # Login Page actions
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        wait = WebDriverWait(driver, 50)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()

        #  PIM actions
        # (// input[@ placeholder='Type for hints...'])[1]

        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//i[@class='oxd-icon bi-chevron-left']")))

        # driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-chevron-left']").click()
        # driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']").click()
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div["
                            "2]/div/div/input").send_keys('Ben Mark')
        driver.find_element(By.XPATH,
                            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i").click()
        # select_list_element = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]")
        time.sleep(3)
        # select_role = Select(select_list_element)
        # select_list_element = driver.find_element(By.XPATH,
        #                                           "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div/")
        # select_role = Select(select_list_element)
        # time.sleep(3)
        # select_role.select_by_index(3)
        time.sleep(3)

    except Exception as e:
        print(e)


def orange_hrm_login():
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)  # 'service_obj' It will update the webdriver library.
    driver.maximize_window()

    # Login Page actions
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(driver, 50)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()

    time.sleep(2)
    # driver.find_element(By.XPATH, "//span[text()='PIM']")
    wait = WebDriverWait(driver, 50)
    wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "PIM")))

    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]").send_keys('Mar')
    time.sleep(5)


if __name__ == "__main__":
    # orange_hrm()
    orange_hrm_login()
