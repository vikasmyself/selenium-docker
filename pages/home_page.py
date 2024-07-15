from utils.custom_parser import getConfig
from base.selenium_driver import SeleniumDriver


class HomePage(SeleniumDriver):
    def __init__(self, driver, wait):
        super(HomePage, self).__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.customer_confirmation_xpath = getConfig("Registration_Page", "customer_confirmation_xpath")
        self.first_name_xpath = getConfig("Registration_Page", "first_name_xpath")
        self.last_name_xpath = getConfig("Registration_Page", "last_name_xpath")
        self.email_xpath = getConfig("Registration_Page", "email_xpath")
        self.password_xpath = getConfig("Registration_Page", "password_xpath")
        self.state_dropdown_xpath = getConfig("Registration_Page", "state_dropdown_xpath")
        self.street_xpath = getConfig("Registration_Page","street_xpath")
        self.city_xpath = getConfig("Registration_Page", "city_xpath")
        self.zip_xpath = getConfig("Registration_Page", "zip_xpath")
    def verify_homepage_loads(self):
        homepage_loads = self.isElementDisplayed(self.customer_confirmation_xpath, "xpath")
        self.screenShot("Home Page Appears")
        return homepage_loads

    def verify_login(self):
        self.sendKeys("test", self.first_name_xpath, "xpath")
        self.sendKeys("test", self.last_name_xpath, "xpath")
        self.sendKeys("test@test.coms",self.email_xpath,"xpath")
        self.sendKeys("test", self.password_xpath,"xpath")
        self.sendKeys("Kadagraha Road, Sompura",self.street_xpath, "xpath")
        self.sendKeys("Bengaluru", self.city_xpath, "xpath")
        self.sendKeys("56212", self.zip_xpath, "xpath")
        self.selectDropdown(self.state_dropdown_xpath, "xpath", visible_text="California")
        self.screenShot("Form filled successfully")