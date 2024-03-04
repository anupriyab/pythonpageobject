import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.RegistrationPage import Registration
from utilities import DataProvider
from Testcases.Test_Base import Test_BaseTest
import logging
from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_Signup(Test_BaseTest):

    @pytest.mark.parametrize("name, phoneNum, email, country, city, username, password",
                             DataProvider.get_data("Sheet1"))
    def test_doSignup(self, name, phoneNum, email, country, city, username, password):
        log.logger.info("Test Sign up started")
        print(username, "------------", password)
        regPage = Registration(self.driver)
        regPage.fillform(name, phoneNum, email, country, city, username, password)
        time.sleep(6)
        log.logger.info("Test Sign up ended")
