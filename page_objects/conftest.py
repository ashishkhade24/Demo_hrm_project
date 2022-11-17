import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import login_details
username=login_details.USERNAME
password=login_details.PASSWORD
import time

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.NAME,"username").send_keys(username)
    time.sleep(1)
    driver.find_element(By.NAME,"password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
    time.sleep(1)
    request.cls.driver=driver











