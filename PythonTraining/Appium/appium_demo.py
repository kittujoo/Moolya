import time
from appium import webdriver
from appium.options.common import AppiumOptions

if __name__ == '__main__':
    appium_server_url = "http://localhost:4723/wd/hub"
    capabilities = dict(
        deviceName='Krushna',
        platformName='Android',
        appPackage='com.androidsample.generalstore',
        appActivity='com.androidsample.generalstore.SplashActivity',
    )
    driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))

    time.sleep(3)
