import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.loginpage import Login

class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

    def test_with_valid_credentials(self):
        lg=Login(self.driver)
        lg.input_username("Admin")
        lg.input_password("admin123")
        lg.enter()

    def test_with_invalid_email(self):
        lg=Login(self.driver)
        lg.input_username("Admn")
        lg.input_password("admin123")
        lg.enter()
        text_read=lg.msg_for_wrong_email()
        print("msg for wrong email_id ",text_read)

    def test_with_invalid_password(self):
        lg = Login(self.driver)
        lg.input_username("Admin")
        lg.input_password("admin12")
        lg.enter()
        text_read = lg.msg_for_wrong_password()
        print("msg for wrong password:", text_read)

    def test_forgot_password(self):
        lg = Login(self.driver)
        lg.forgot_pass_word()

    def tearDown(self) -> None:
        self.driver.quit()









