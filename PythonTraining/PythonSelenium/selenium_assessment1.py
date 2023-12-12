from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def cric_info_trending_player_screenshot(self, image_name):
    try:
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)  # 'service_obj' It will update the webdriver library.
        driver.get("https://www.espncricinfo.com/")
        driver.maximize_window()
        print(driver.title)
        driver.implicitly_wait(10)
        go_to_trending_players = driver.find_element(By.XPATH, "//span[contains(text(), 'Trending Players')]")
        driver.implicitly_wait(10)
        driver.execute_script("arguments[0].scrollIntoView();", go_to_trending_players)
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            "//i[@class='icon-keyboard_arrow_right-outlined ds-text-icon ds-ml-1']").click()
        time.sleep(3)
        driver.save_screenshot(image_name + ".png")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    cric_info_trending_player_screenshot("trending_player")
