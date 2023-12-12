from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

"""
    Day3 selenium
    Frames
    explicit wait
"""


def get_connection(url, browser):
    service_obj = Service()
    driver = None
    if browser == 'Chrome':
        driver = webdriver.Chrome(service=service_obj)  # 'service_obj' It will update the webdriver library.
    elif browser == 'Firefox':
        driver = webdriver.Firefox(service=service_obj)
    elif browser == 'Edge':
        driver = webdriver.Edge(service=service_obj)
    driver.get(url)
    driver.maximize_window()
    # print(driver.title)
    return driver


# driver = get_connection("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 'Chrome')
# wait = WebDriverWait(driver, 50)
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.CSS_SELECTOR,".oxd-button").click()
#
# wait = WebDriverWait(driver, 20)
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//i[@class='oxd-icon bi-chevron-left']")))
# driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-chevron-left']").click()
# time.sleep(3)


# // a[ @ id = 'opentab']
# dr = get_connection("https://rahulshettyacademy.com/AutomationPractice/", 'Chrome')
# dr.implicitly_wait(15)
# dr.find_element(By.XPATH, "// a[ @ id = 'opentab']").click()
# time.sleep(3)
# current_url = dr.current_url
# print(dr.title)
# print(current_url)
#
# current_window = dr.current_window_handle
# all_active_windows = dr.window_handles
#
# for window in all_active_windows:
#     if current_window != window:
#         dr.switch_to.window(window)
#         print(dr.title)
#         print(dr.current_url)

# openwindow
# dr = get_connection("https://rahulshettyacademy.com/AutomationPractice/", 'Chrome')
# dr.implicitly_wait(15)
# dr.find_element(By.ID, "openwindow").click()
#
# current_url = dr.current_url
# print(dr.title)
# print(current_url)
#
# current_window = dr.current_window_handle
# all_active_windows = dr.window_handles
#
# for window in all_active_windows:
#     if current_window != window:
#         dr.switch_to.window(window)
#         print(dr.title)
#         print(dr.current_url)


# driver = get_connection("https://the-internet.herokuapp.com/windows", 'Chrome')
# driver.implicitly_wait(15)
# driver.find_element(By.LINK_TEXT, 'Click Here').click()
# time.sleep(3)
# windows_opened = driver.window_handles
# print(windows_opened)
# driver.switch_to.window(windows_opened[1])
# print(driver.find_element(By.TAG_NAME, 'h3').text)
# time.sleep(3)
# driver.switch_to.window(windows_opened[0])
# print(driver.find_element(By.TAG_NAME, 'h3').text)
# time.sleep(3)


# driver = get_connection("https://demoqa.com/frames", 'Chrome')
# driver.implicitly_wait(10)
# driver.switch_to.frame('frame1')
# print(driver.find_element(By.ID, 'sampleHeading').text)
# driver.switch_to.default_content()
# print(driver.title)

# driver = get_connection("https://rahulshettyacademy.com/AutomationPractice/", 'Chrome')
# driver.implicitly_wait(10)
# idval = driver.find_element(By.NAME, 'iframe-name')
# time.sleep(3)
# driver.execute_script("arguments[0].scrollIntoView();",idval)
# time.sleep(3)
# print(idval.text)
# driver.switch_to.frame('iframe-name')
# print(driver.title)
# time.sleep(3)
# driver.switch_to.default_content()
# print(driver.title)

driver = get_connection("https://rahulshettyacademy.com/AutomationPractice/", 'Chrome')
driver.implicitly_wait(10)
print(driver.find_element(By.XPATH, "//div[@class='tableFixHead']/table/tbody/tr[2]/td[3]").text)
print(driver.find_element(By.XPATH, "//div[@class='tableFixHead']/table/tbody/tr[2]/td[3]/preceding-sibling::td[2]").text)
print(driver.find_element(By.XPATH, "//div[@class='tableFixHead']/table/tbody/tr[2]/td[3]/following-sibling::td[1]").text)
print(driver.find_element(By.XPATH, "//div[@class='tableFixHead']/table/tbody/tr[2]/td[3]/../td[1]").text)
table_data = driver.find_element(By.XPATH, "//div[@class='tableFixHead']/table")
# json = driver.execute_script("return arguments[0].innerText;",table_data)
# print(json)
# print(driver.execute_script("return arguments[0].innerText;",table_data))
data = driver.execute_script("return arguments[0].innerText;",table_data)
print(type(data))
print(data)
