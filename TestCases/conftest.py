from encodings import undefined

import pytest
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait

from utilities import ConfigReader
from utilities.ConfigReader import readconfig


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def launch_browser(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    if request.param == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver = driver

    driver.get(ConfigReader.readconfig("basic info", "testingurl"))
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()
