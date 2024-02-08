from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from utilities import ConfigReader


class Registration(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fillform(self, name, phoneNum, email, country, city, username, password):
        # self.driver.findelement(By.XPATH, ConfigReader.readconfig("locator_RegistrationPage", "name_Xpath")).send_Keys(   name)
        self.enterValue("name_Xpath", name)
        self.enterValue("phone_Xpath", phoneNum)
        self.enterValue("email_Xpath", email)
        self.enterValue("city_Xpath", city)
        self.enterValue("username_Xpath", username)
        self.enterValue("password_Xpath", password)
        self.select("country_Xpath",country)
        self.click("submit_Xpath")
