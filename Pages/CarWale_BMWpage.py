from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from utilities import ConfigReader


class BMWPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def getTitle(self):
        return self.driver.find_element(By.XPATH,
                                        ConfigReader.readconfig("carwale_Locators", "cars_Title_Xpath"))
