import time
from selenium.webdriver.common.by import By
from page_objects.base import Base

class Pay_Grade(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    job_tab = (By.XPATH, "//span[normalize-space()='Job']")
    pay_grade_tab=(By.XPATH,"//ul[@class='oxd-dropdown-menu']/li[2]")
    add_button=(By.XPATH,"//button[normalize-space()='Add']")
    input_field=(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
    save_button=(By.XPATH,"//button[normalize-space()='Save']")
    cancel_button_tab=(By.XPATH,"//button[normalize-space()='Cancel']")
    select_emp=(By.XPATH,"//div[@role='table']//div[1]//div[1]//div[1]//div[1]//div[1]//label[1]//span[1]")
    delete_select=(By.XPATH,"//button[normalize-space()='Delete Selected']")
    no_cancel=(By.XPATH,"//button[normalize-space()='No, Cancel']")
    delete_buttton=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/button[1]")
    yes_delete=(By.XPATH,"//button[normalize-space()='Yes, Delete']")


    def goto_pay_grade(self):
        self.navigate_to_tab(self.Admin_tab)
        self.EF.find_element(self.job_tab).click()
        self.EF.find_element(self.pay_grade_tab).click()

    def add_grade(self):
        self.goto_pay_grade()
        self.EF.find_element(self.add_button).click()
        self.EF.find_element(self.input_field).send_keys("Ashish")
        self.EF.find_element(self.save_button).click()

    def cancel_button(self):
        self.goto_pay_grade()
        self.EF.find_element(self.add_button).click()
        self.EF.find_element(self.input_field).send_keys("grade_ash")
        self.EF.find_element(self.cancel_button_tab).click()

    def delete_emp(self):

        self.goto_pay_grade()
        self.EF.find_element(self.select_emp).click()
        self.EF.find_element(self.delete_select).click()
        self.EF.find_element(self.no_cancel).click()
        self.EF.find_element(self.select_emp).click()
        self.EF.find_element(self.delete_buttton).click()
        self.EF.find_element(self.yes_delete).click()
        time.sleep(3)
        self.driver.close()




