import time
from selenium.webdriver.common.by import By
from page_objects.base import Base
from selenium.webdriver import ActionChains

class Configuration(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    conf_tab=(By.XPATH,"//span[@class='oxd-topbar-body-nav-tab-item']")
    custom_field=(By.XPATH,"//a[normalize-space()='Custom Fields']")
    add_button=(By.XPATH,"//button[normalize-space()='Add']")
    Field_name=(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
    screen_tab=(By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//div[@class='oxd-select-text oxd-select-text--active']")
    type_tab=(By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters organization-name-container']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//div[@class='oxd-select-text oxd-select-text--active']")
    save_button=(By.XPATH,"//button[normalize-space()='Save']")
    cancel_button=(By.XPATH,"//button[normalize-space()='Cancel']")
    tick=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]")
    delete_select=(By.XPATH,"//button[normalize-space()='Delete Selected']")
    yes_delete=(By.XPATH,"//button[normalize-space()='Yes, Delete']")
    edit_button=(By.XPATH,"//div[@role='table']//div[1]//div[1]//div[5]//div[1]//button[2]")


    def goto_custom_field(self):
        # self.navigate_to_tab(self.Pim_tab)
        self.EF.find_element(self.conf_tab).click()
        self.EF.find_element(self.custom_field).click()

    def add_field(self,field):
        self.EF.find_element(self.add_button).click()
        self.EF.find_element(self.Field_name).send_keys(field)

    def select_screen(self):
        self.EF.find_element(self.screen_tab).click()
        drop_down=self.driver.find_element(By.XPATH,"//*[text()='Personal Details']")
        actions=ActionChains(self.driver)
        actions.click(on_element=drop_down)
        time.sleep(2)
        actions.perform()

    def type_select(self):
        self.EF.find_element(self.type_tab).click()
        dropdown_element=self.driver.find_element(By.XPATH,"//*[text()='Text or Number']")
        actions=ActionChains(self.driver)
        actions.click(on_element=dropdown_element)
        time.sleep(3)
        actions.perform()

    def save_button_click(self):
        self.EF.find_element(self.save_button).click()

    def cancel_button_click(self):
        self.EF.find_element(self.cancel_button).click()

    def check_custom_field(self):
        self.goto_custom_field()
        self.add_field("any field")
        self.select_screen()
        self.type_select()
        self.save_button_click()

    def check_cancel_button(self):
        self.goto_custom_field()
        self.add_field("any field")
        self.select_screen()
        self.type_select()
        self.cancel_button_click()

    def delete_user(self):

        self.goto_custom_field()
        self.EF.find_element(self.tick).click()
        self.EF.find_element(self.delete_select).click()
        self.EF.find_element(self.yes_delete).click()





