import time
from selenium.webdriver.common.by import By
from page_objects.base import Base
from selenium.webdriver import ActionChains
from utility.elementry_functions import Elem_Func
from selenium.webdriver.support.select import Select

class Users(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    user_management_link=(By.XPATH,"//li[@class='oxd-topbar-body-nav-tab --parent --visited']")
    users_link=(By.XPATH,"//a[normalize-space()='Users']")
    enter_username_txt=(By.XPATH,"//label[text()='Username']/../..//input")
    select_user=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]")
    enter_employee_name_txt=(By.XPATH,"//input[@placeholder='Type for hints...']")
    select_user_status=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]")
    click_search=(By.XPATH, "//button[normalize-space()='Search']")

    def goto_users_page(self):
        self.navigate_to_tab(self.Admin_tab)
        self.EF.find_element(self.user_management_link).click()
        self.EF.find_element(self.users_link).click()

    def enter_username(self):
        self.EF.find_element(self.enter_username_txt).send_keys("Nathan.Elliot")
        time.sleep(3)

    def select_user_role(self):
        self.EF.find_element(self.select_user).click()
        time.sleep(3)
        dropdown_element = self.driver.find_element(By.XPATH, "//*[text()='ESS']")
        actions = ActionChains(self.driver)
        actions.click(on_element=dropdown_element)
        time.sleep(2)
        actions.perform()
        time.sleep(3)

    def enter_employee_name(self, employee_name):
        self.EF.find_element(self.enter_employee_name_txt).send_keys(employee_name)

    def select_status(self):
        self.EF.find_element(self.select_user_status).click()
        dropdown_element = self.driver.find_element(By.XPATH, "//*[text()='Enabled']").click()
        actions = ActionChains(self.driver)
        actions.click(on_element=dropdown_element)
        time.sleep(2)
        actions.perform()
        time.sleep(5)

    def click_search_btn(self):
        self.EF.find_element(self.click_search).click()
        time.sleep(3)

    def search_user(self):
        self.goto_users_page()
        self.enter_username()
        self.select_user_role()
        self.enter_employee_name("Nathan Elliot")
        self.select_status()
        self.click_search_btn()
        print("click successfully")










