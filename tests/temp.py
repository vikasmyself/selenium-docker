from selenium import webdriver

class TestWebDriverFactory:
    browser = "chrome"

    def test_getWebDriverInstance(self):
        hubURL = "http://localhost:4444/wd/hub"
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Remote(command_executor=hubURL, options=options)

        driver.get("http://www.google.com")
        print(driver.title)  # Should print "Google"
        driver.quit()
