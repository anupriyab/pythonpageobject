from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from utilities import ConfigReader


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def dologin(self):
        pass
