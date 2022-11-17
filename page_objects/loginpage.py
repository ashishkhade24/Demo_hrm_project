from page_objects.base import Base
from selenium.webdriver.common.by import By
class Login(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    Username_demo=(By.XPATH,"//input[@placeholder='Username']")
    Password_demo=(By.XPATH,"//input[@placeholder='Password']")
    click=(By.XPATH,"//button[normalize-space()='Login']")
    wrong_credentials=(By.XPATH,"//div[@role='alert']")
    forgot_password=(By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
    page=(By.XPATH,"//div[@class='orangehrm-card-container']")
    user_forgot=(By.XPATH,"//input[@placeholder='Username']")
    reset_button=(By.XPATH,"//button[normalize-space()='Reset Password']")

    def input_username(self,username):
        self.EF.find_element(self.Username_demo).send_keys(username)

    def input_password(self,password):
        self.EF.find_element(self.Password_demo).send_keys(password)

    def enter(self):
        self.EF.find_element(self.click).click()

    def msg_for_wrong_email(self):
        return self.EF.find_element(self.wrong_credentials).text

    def msg_for_wrong_password(self):
        return self.EF.find_element(self.wrong_credentials).text

    def forgot_pass_word(self):
        self.EF.find_element(self.forgot_password).click()
        self.EF.find_element(self.page)
        self.EF.find_element(self.user_forgot).send_keys("Admin")
        self.EF.find_element(self.reset_button).click()








