from Pages.BasePage import BasePage
from Pages.CarWale_NewcarPage import NewCarPage

class Homepage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def selectnewcar(self):
        self.mouseHover("Newcar_Xpath")
        self.click("FindNewCar_Xpath")
        return NewCarPage(self.driver)

