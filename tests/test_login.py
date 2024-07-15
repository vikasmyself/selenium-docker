from pages.home_page import HomePage
import pytest


@pytest.mark.usefixtures("oneTimeSetup")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, oneTimeSetup):
        self.driver = oneTimeSetup
        self.homepage = HomePage(self.driver, self.wait)

    def test_homepage_appears(self):
        homepage_loads = self.homepage.verify_homepage_loads()
        assert homepage_loads is True

    def test_login(self):
        self.homepage.verify_login()
