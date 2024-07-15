from pages.home_page import HomePage
import pytest, allure


@allure.feature('Login Feature')
@allure.story('user logs in Successfully')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("oneTimeSetup")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, oneTimeSetup):
        self.driver = oneTimeSetup
        self.homepage = HomePage(self.driver, self.wait)

    @allure.step('Verify Login page appears')
    def test_homepage_appears(self):
        homepage_loads = self.homepage.verify_homepage_loads()
        assert homepage_loads is True

    @allure.step('Verify Login Succefully')
    def test_login(self):
        self.homepage.verify_login()
