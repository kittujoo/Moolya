from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


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
    driver.implicitly_wait(10)
    driver.maximize_window()

    # print(driver.title)
    return driver


def drop_down_example(dr):
    dd = Select(dr.find_element(By.ID, "dropdown-class-example"))
    time.sleep(3)
    dd.select_by_index(3)
    time.sleep(3)
    dd.select_by_value("option2")
    time.sleep(3)
    dd.select_by_value("option1")
    time.sleep(3)


def dynamic_drop_down_example(dr):
    dr.implicitly_wait(10)
    dd = dr.find_element(By.ID, 'autocomplete').send_keys('ind')
    bool_dd = dr.find_element(By.ID, 'autocomplete').is_displayed()
    print(bool_dd)
    atr_dd = dr.find_element(By.ID, 'autocomplete').get_attribute('value')
    print(atr_dd)
    # time.sleep(3)
    countries = dr.find_elements(By.XPATH, "//ul[@id = 'ui-id-1']//li//div")

    for county in countries:
        if county.text == 'India':
            print()

            county.click()

            # break

    as_dd = dr.find_element(By.ID, 'autocomplete').get_attribute('value')
    print(as_dd)
    assert as_dd == 'India'


def check_box_example(dr):
    check_box_element = dr.find_element(By.ID, 'checkBoxOption1')
    print(check_box_element.is_selected())
    check_box_element.click()
    print(check_box_element.is_selected())
    ele = dr.find_elements(By.XPATH, "//input[@type='checkbox']")
    # print(len(ele))

    for el in ele:
        if el.get_attribute('value') == 'option1':
            el.click()
            print('asserted')
            print(el.is_selected())
            assert el.is_selected()


def driver_manger_function(dr):
    dr.implicitly_wait(10)
    dr.find_element(By.ID, "alertbtn").click()
    alt = dr.switch_to.alert
    alert_text = alt.text
    print(alert_text)
    message = "Hello , share this practice page and share your knowledge"
    assert alert_text == message
    alt.accept()
    alt.dismiss()


def actions_example(dr):
    action = ActionChains(dr)
    action.move_to_element(dr.find_element(By.ID, 'mousehover')).perform()
    dr.implicitly_wait(10)
    action.key_down(Keys.ARROW_DOWN).perform()
    action.context_click(dr.find_element(By.LINK_TEXT, 'Top')).perform()
    action.key_down(Keys.ENTER).perform()
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    action.key_down(Keys.CONTROL, 'a').key_up(Keys.CONTROL).perform()


def actions_example_drag_and_drop(dr):
    action = ActionChains(dr)
    dr.implicitly_wait(10)
    # src = action.move_to_element(dr.find_element(By.ID, 'draggable'))
    # dest = action.move_to_element(dr.find_element(By.ID, 'droppable'))
    src = (dr.find_element(By.ID, 'draggable'))
    dest = (dr.find_element(By.ID, 'droppable'))
    action.drag_and_drop(src, dest)
    time.sleep(3)

    dr = get_connection("https://demoqa.com/buttons", 'Chrome')
    action.click(dr.find_element(By.ID, 'doubleClickBtn')).perform()
    time.sleep(3)


if __name__ == "__main__":
    dr = get_connection("https://rahulshettyacademy.com/AutomationPractice/", 'Chrome')
    # print(dr.title)
    # print(dr.current_url)
    # drop_down_example(dr)
    dynamic_drop_down_example(dr)
    # check_box_example(dr)
    # driver_manger_function(dr)
    # actions_example(dr)
    # dr = get_connection("https://demoqa.com/droppable", 'Chrome')
    # actions_example_drag_and_drop(dr)

    # """Buttons"""
    # dr = get_connection("https://demoqa.com/buttons", 'Chrome')
    # dr.implicitly_wait(10)
    # action = ActionChains(dr)
    # action.click(dr.find_element(By.ID, 'doubleClickBtn')).perform()
    # time.sleep(3)
    # action.click(dr.find_element(By.ID, 'rightClickBtn')).perform()
    # time.sleep(3)
    # action.click(dr.find_element(By.ID, 'XbvYI')).perform()
    # time.sleep(3)

    # javascript
    # dr = get_connection("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 'Chrome')
    # dr.implicitly_wait(15)
    # name = dr.find_element(By.NAME, 'username')
    # dr.execute_script("arguments[0].value='Admin';",name)
    # time.sleep(3)
    # pwd = dr.find_element(By.NAME, 'password')
    # dr.execute_script("arguments[0].value='admin123';", pwd)
    # time.sleep(3)
    # submit = dr.find_element(By.CSS_SELECTOR,".oxd-button")
    # dr.execute_script("arguments[0].click();", submit)
    # time.sleep(6)

    # scrolling
    # dr = get_connection("https://rahulshettyacademy.com/AutomationPractice/", 'Chrome')
    # dr.implicitly_wait(15)
    # # dr.execute_script("window.scrollBy(0,800);")
    # dr.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    # time.sleep(3)
    # dr.execute_script("window.scrollBy(0,-document.body.scrollHeight);")
    # time.sleep(3)

    # scrolling with elements
    # dr = get_connection("https://rahulshettyacademy.com/AutomationPractice/", 'Chrome')
    # dr.implicitly_wait(15)
    # # idval = dr.find_element(By.XPATH, "//div[contains(text(), Neha Manoj)]")
    # idval = dr.find_element(By.ID, 'mousehover')
    # time.sleep(3)
    # dr.execute_script("arguments[0].scrollIntoView();",idval)
    # time.sleep(3)
    # print(idval.text)

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

    pass