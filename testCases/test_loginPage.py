import pytest
from pageObjects.Login import LoginPage

class TestLogin:
    baseURL = 'https://www.travelio.com/'

    def setup_page(self, driver):
        driver.get(self.baseURL)
        driver.implicitly_wait(10)
        lp = LoginPage(driver)
        act_title = driver.title
        return act_title

    def test_TC_001_REGISTER_002(self, setup):
        self.driver = setup
        self.setup_page(self.driver)
        lp = LoginPage(self.driver)
        lp.success_login()
