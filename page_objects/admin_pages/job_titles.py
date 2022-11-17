import time
from selenium.webdriver.common.by import By
from page_objects.base import Base
from selenium.webdriver import ActionChains
from utility.elementry_functions import Elem_Func

class JOB(Base):
    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    job_tab=(By.XPATH,"//span[normalize-space()='Job']")
    job_title=(By.XPATH,"//ul[@class='oxd-dropdown-menu']/li[1]")
    add_button=(By.XPATH,"//button[normalize-space()='Add']")
    add_job_title=(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
    add_description=(By.XPATH,"//textarea[@placeholder='Type description here']")
    save_button=(By.XPATH,"//button[normalize-space()='Save']")
    select_user=(By.XPATH,"//div[@role='table']//div[1]//div[1]//div[1]//div[1]//div[1]//label[1]//span[1]")
    delete_button=(By.XPATH,"//button[normalize-space()='Delete Selected']")
    yes_button=(By.XPATH,"//div[@role='document']/div/button[2]")
    delete_option=(By.XPATH,"//div[@role='table']//div[1]//div[1]//div[4]//div[1]//button[1]//i[1]")
    edit_button=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/button[2]")

    def goto_job_title_page(self):
        self.navigate_to_tab(self.Admin_tab)
        self.EF.find_element(self.job_tab).click()
        self.EF.find_element(self.job_title).click()

    def goto_job_title(self):
        self.goto_job_title_page()
        self.EF.find_element(self.add_button).click()
        self.EF.find_element(self.add_job_title).send_keys("admin3")
        self.EF.find_element(self.add_description).send_keys("good")
        self.EF.find_element(self.save_button).click()
        self.driver.refresh()
        self.driver.back()

    def delete_select(self):
        self.goto_job_title_page()
        self.EF.find_element(self.select_user).click()
        self.EF.find_element(self.delete_button).click()
        self.EF.find_element(self.yes_button).click()

    def delete_btn(self):
        self.goto_job_title_page()
        self.EF.find_element(self.delete_option).click()
        self.EF.find_element(self.yes_button).click()

    def edit_option(self):
        self.goto_job_title_page()
        self.EF.find_element(self.edit_button).click()
        self.EF.find_element(self.add_job_title).send_keys("admin6")
        self.EF.find_element(self.add_description).send_keys("greatest")
        self.EF.find_element(self.save_button).click()




