from Pages.BasePage import BasePage


class NewCarPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def selectBMW(self):
        self.click("BmW_Xpath")

    def selectToyato(self):
        self.click("Toyota_Xpath")