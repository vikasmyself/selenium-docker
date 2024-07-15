from selenium import webdriver
from webdriver_manager.drivers import edge, firefox, chrome
from utils.custom_parser import *


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = getConfig("Setup","baseURL")
        if self.browser == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--disable-infobars")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("disable-infobars")
            options.add_argument("--disable-plugins-discovery")
            options.add_argument("--disable-extensions")

            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
            options.add_experimental_option("prefs", prefs)
            driver = webdriver.Edge(options=options)
        elif self.browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--disable-infobars")
            #options.add_experimental_option("excludeSwitches", ["enable-automation"])
            #options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("disable-infobars")
            options.add_argument("--disable-plugins-discovery")
            options.add_argument("--disable-extensions")
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
            #options.add_experimental_option("prefs", prefs)
            driver = webdriver.Firefox(options=options)
        elif self.browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-infobars")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("disable-infobars")
            options.add_argument("--disable-plugins-discovery")
            options.add_argument("--disable-extensions")
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1280,1024")
            options.add_argument("--remote-debugging-port=9222")
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
            options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(options=options)
        else:
            print("Launching the default driver, Chrome ..")
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-infobars")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("disable-infobars")
            options.add_argument("--disable-plugins-discovery")
            options.add_argument("--disable-extensions")
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1280,1024")
            options.add_argument("--remote-debugging-port=9222")
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
            options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        return driver
