from selenium.webdriver.common.by import By
from utility.elementry_functions import Elem_Func
class Base:
    def __init__(self,driver):
        self.driver=driver
        self.EF=Elem_Func(self.driver)

    Admin_tab=(By.XPATH,"//a[contains(@href,'viewAdminModule')]")
    Pim_tab=(By.XPATH,By.XPATH,"//a[contains(@href,'viewPimModule']")
    leave_tab=(By.XPATH,"//a[contains(@href,'viewLeaveModule']")
    User_profile=(By.CLASS_NAME, 'oxd-userdropdown')
    Log_out=(By.LINK_TEXT, "Logout")

    def click_user_profile(self):
        self.EF.find_element(self.User_profile).click()

    def click_logout_link(self):
        self.EF.find_element(self.Log_out).click()

    def logout(self):
        self.click_user_profile()
        self.click_logout_link()

    def navigate_to_tab(self,tab_link):
        self.EF.find_element(tab_link).click()




