from selenium.webdriver.common.by import By
import time
from page_objects.base import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Add_Employees(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    add_emp_button=(By.XPATH,"//a[normalize-space()='Add Employee']")
    first_name=(By.XPATH,"//input[@placeholder='First Name']")
    middle_name=(By.XPATH,"//input[@placeholder='Middle Name']")
    last_name=(By.XPATH,"//input[@placeholder='Last Name']")
    emp_id=(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
    toggle=(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    user_name=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]")
    password=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]")
    confirm_password=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/input[1]")
    save_button=(By.XPATH,"//button[normalize-space()='Save']")

    def add_emp(self):
        self.EF.find_element(self.add_emp_button).click()
        self.EF.find_element(self.first_name).send_keys("Ashu")
        self.EF.find_element(self.middle_name).send_keys("king")
        self.EF.find_element(self.last_name).send_keys("kumar")
        id=self.EF.find_element(self.emp_id)
        id.send_keys(Keys.CONTROL+"a")
        id.send_keys(Keys.BACKSPACE)
        id.send_keys("1234")
        print("1234")
        self.EF.find_element(self.toggle).click()
        user=self.EF.find_element(self.user_name)
        user.send_keys(Keys.CONTROL+"a")
        user.send_keys(Keys.BACKSPACE)
        user.send_keys("Admin11")
        password_d=self.EF.find_element(self.password)
        password_d.send_keys(Keys.CONTROL+"a")
        password_d.send_keys(Keys.BACKSPACE)
        password_d.send_keys("admin145")
        self.EF.find_element(self.confirm_password).send_keys("admin145")
        self.EF.find_element(self.save_button).click()
        self.driver.back()








