from encodings import undefined

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ConfigReader


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, launch_browser):
    yield
    item = request.node
    driver1 = launch_browser
    if item.rep_call.failed:
        allure.attach(driver1.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["chrome", "firefox"], scope="class")
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
