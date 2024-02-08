import time

from Pages.Carwale_Homepage import Homepage
from TestCases.Test_Base import Test_BaseTest
import logging

from utilities import DataProvider
from utilities.LogUtil import Logger
import pytest

log = Logger(__name__, logging.INFO)


class Test_Carwale(Test_BaseTest):

    @pytest.mark.skip
    def test_newcar(self):
        log.logger.info("Test new car started")
        Home = Homepage(self.driver)
        Home.selectnewcar()
        time.sleep(4)
        log.logger.info("Test new car ended")

    @pytest.mark.parametrize("carbrand", DataProvider.get_data("newcar"))
    def test_selectcars(self, carbrand):
        log.logger.info("Test selecting new car started")
        Home = Homepage(self.driver)
        Home.selectnewcar()
        if carbrand == "BMW":
            Home.selectnewcar().selectBMW()
        elif carbrand == "Toyato":
            Home.selectnewcar().selectToyato()

        time.sleep(4)
        log.logger.info("Test selecting new car ended")
