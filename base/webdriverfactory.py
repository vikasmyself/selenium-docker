from selenium import webdriver
from utils.custom_parser import getConfig


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def _set_common_options(self, options):
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1280,1024")

    def getWebDriverInstance(self):
        baseURL = getConfig("Setup", "baseURL")
        hubURL = getConfig("Setup", "hub_url")
        selenium_grid = getConfig("Setup","selenium_grid")

        if self.browser == "chrome":
            options = webdriver.ChromeOptions()
            self._set_common_options(options)
            if selenium_grid.lower() == "true":
                print("Started executing in grid ...")
                driver = webdriver.Remote(command_executor=hubURL, options=options)
            else:
                driver = webdriver.Chrome(options=options)

        elif self.browser == "firefox":
            options = webdriver.FirefoxOptions()
            self._set_common_options(options)
            driver = webdriver.Remote(command_executor=hubURL, options=options)

        elif self.browser == "edge":
            options = webdriver.EdgeOptions()
            self._set_common_options(options)
            driver = webdriver.Remote(command_executor=hubURL, options=options)

        else:
            raise ValueError(f"Unsupported browser: {self.browser}")

        driver.maximize_window()
        driver.get(baseURL)
        return driver
