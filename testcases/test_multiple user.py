from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Chromeservice
from selenium.webdriver.common.keys import Keys

test_data=[
            ["Admin", "admin123"],
            ["Admin", "admin123"],
            ["Admin", "admin123"],
            ["Admin", "admin123"],
            ["Admin", "admin123"],
            ["Admin", "admin123"],
           ]

@pytest.mark.parametrize("username,password",test_data)
def test_login(username,password):
    driver = webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(Keys.CONTROL+"a")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(Keys.CONTROL+"a")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(password)
    driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
    time.sleep(3)
    driver.quit()





