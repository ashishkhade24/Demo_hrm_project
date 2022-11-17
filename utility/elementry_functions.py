import random
import sys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class Elem_Func:

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,locator_tuple):
        try:
            element = WebDriverWait(self.driver, 10, poll_frequency=1).until(
                EC.presence_of_element_located(locator_tuple))
            return element
        except:
            self.screen_shot()
            raise

    def mouse_hover(self, locator_tuple):
        element = self.find_element(locator_tuple)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

