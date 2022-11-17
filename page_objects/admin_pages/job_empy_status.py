from page_objects.base import Base
import time
from selenium.webdriver.common.by import By

class Emp_Status(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    job_tab = (By.XPATH, "//span[normalize-space()='Job']")
    empl_tab=(By.XPATH,"//ul[@class='oxd-dropdown-menu']/li[3]")
    add_tab=(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    input_field=(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
    submit_button=(By.XPATH,"//button[@type='submit']")
    cancel_button=(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--ghost']")
    delete_button=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[5]/div[1]/div[3]/div[1]/button[1]/i[1]")
    yes_delete=(By.XPATH,"//button[normalize-space()='Yes, Delete']")

    def add_employee(self):
        self.navigate_to_tab(self.Admin_tab)
        self.EF.find_element(self.job_tab).click()
        self.EF.find_element(self.empl_tab).click()
        self.EF.find_element(self.add_tab).click()
        self.EF.find_element(self.input_field).send_keys("king2")
        self.EF.find_element(self.submit_button).click()

    def check_cancel(self):
        self.navigate_to_tab(self.Admin_tab)
        self.EF.find_element(self.job_tab).click()
        self.EF.find_element(self.empl_tab).click()
        self.EF.find_element(self.add_tab).click()
        self.EF.find_element(self.input_field).send_keys("king2")
        self.EF.find_element(self.cancel_button).click()
        self.EF.find_element(self.delete_button).click()
        self.EF.find_element(self.yes_delete).click()

