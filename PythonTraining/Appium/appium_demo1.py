import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

if __name__ == '__main__':
    appium_server_url = "http://localhost:4723/wd/hub"
    capabilities = dict(
        deviceName='Krushna',
        platformName='Android',
        appPackage='com.androidsample.generalstore',
        appActivity='com.androidsample.generalstore.SplashActivity',
    )
    drop_down_locator_country = (AppiumBy.ID, "android:id/text1")
    drop_down_locator = (By.ID, "com.androidsample.generalstore:id/spinnerCountry")
    name_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/nameField")
    radio_locator = (AppiumBy.ID, "com.androidsample.generalstore:id/radioFemale")
    text_select = (AppiumBy.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]")
    driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
    time.sleep(3)
    driver.find_element(*drop_down_locator).click()
    time.sleep(3)
    # country_items = (AppiumBy.XPATH, "//android.widget.TextView")
    # time.sleep(3)
    # country_list = driver.find_elements(*country_items)
    is_country_found = True
    while is_country_found:
        # driver.find_element(*drop_down_locator).click()
        # time.sleep(1)
        country_items = (By.XPATH, "//android.widget.TextView")
        time.sleep(1)
        country_list = driver.find_elements(*country_items)
        print(len(country_list))
        for country in country_list:
            print(country.text)
            if country.text == 'India':
                # print(country.text)
                is_country_found = False
                country.click()
                break

        # driver.swipe(789, 2088, 178, 595, 500)
        # driver.swipe(263, 2060, 263, 2060, 500)
        driver.swipe(535, 2054, 389, 676, 500)
                # print(country.text)
                # time.sleep(.1)


    # driver.swipe(204, 1543, 334, 1544, 500)
    # count = 0
    # for i in range(650, 16000, 1203):
    #     count = count + 1
    #     print(count)
    #     driver.find_element(*drop_down_locator).click()
    #     driver.swipe(263, 2000, 263, 2000, 500)
    #
    #     time.sleep(.01)

    # print(driver.find_element(*text_select).text)
    # driver.swipe(204, 1543, 334, 1544, 500)
    # while True:

    # driver.scroll('afghanistan', 'india',500)
    # driver.find_element(*drop_down_locator_country).click()
    # select_dropdown = Select(driver.find_element(*drop_down_locator))
    # select_dropdown = driver.find_element(*drop_down_locator)
    # select = Select(select_dropdown)
    # driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/spinnerCountry").click()
    # time.sleep(3)
    # select.select_by_index(2)
    # time.sleep(3)
    driver.find_element(*name_locator).send_keys("Krushna")
    time.sleep(3)
    driver.find_element(*radio_locator).click()
    time.sleep(3)
    driver.swipe(240, 1524, 511, 1524, 500)  # 196,703,287,711
    # 240, 1524, 511, 1524
    time.sleep(3)
