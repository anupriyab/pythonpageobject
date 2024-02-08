from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.LogUtil import Logger
from utilities import ConfigReader
import logging
from selenium.webdriver.common.action_chains import ActionChains
log= Logger(__name__,logging.INFO)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_Xpath"):
            self.driver.find_element(By.XPATH, ConfigReader.readconfig("carwale_Locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR,
                                    ConfigReader.readconfig("locator_RegistrationPage", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, ConfigReader.readconfig("locator_RegistrationPage", locator)).click()

        log.logger.info("clicking onthe element"+ str(locator))

    def enterValue(self, locator, value):
        if str(locator).endswith("_Xpath"):
            self.driver.find_element(By.XPATH,
                                    ConfigReader.readconfig("locator_RegistrationPage", locator)).send_keys(
                value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR,
                                    ConfigReader.readconfig("locator_RegistrationPage", locator)).send_keys(
                value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, ConfigReader.readconfig("locator_RegistrationPage", locator)).send_keys(
                value)
        log.logger.info(" entering  i nthe element" + str(locator)+ "value ---"+str(value))
    def select(self, locator, value):


        if str(locator).endswith("_Xpath"):
            dropdown = self.driver.find_element(By.XPATH, ConfigReader.readconfig("locator_RegistrationPage", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR,ConfigReader.readconfig("locator_RegistrationPage", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element(By.ID, ConfigReader.readconfig("locator_RegistrationPage", locator))

        select = Select(dropdown)
        select.select_by_visible_text(value)
        log.logger.info(" Selecting on the element" + str(locator) + "value ---" + str(value))

    def mouseHover(self, locator):

            if str(locator).endswith("_Xpath"):
                ele = self.driver.find_element(By.XPATH,
                                                    ConfigReader.readconfig("carwale_Locators", locator))
            elif str(locator).endswith("_CSS"):
                ele = self.driver.find_element(By.CSS_SELECTOR,
                                                    ConfigReader.readconfig("carwale_Locators", locator))
            elif str(locator).endswith("_ID"):
                ele = self.driver.find_element(By.ID, ConfigReader.readconfig("carwale_Locators", locator))

            Action =  ActionChains(self.driver)
            Action.move_to_element(ele).perform()
            log.logger.info(" mouse hove  on the element" + str(locator) )