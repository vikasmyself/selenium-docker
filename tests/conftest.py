import pytest, os
from base.webdriverfactory import WebDriverFactory
from selenium.webdriver.support.ui import WebDriverWait
import time


@pytest.fixture(scope='class')
def oneTimeSetup(request, browser, osType):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    wait = WebDriverWait(driver, 50)

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.wait = wait
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser. E.g. chrome, firefox")
    parser.addoption("--osType", action="store", default="windows", help="Type of operating system. E.g. windows, linux, mac")


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption("--osType")
