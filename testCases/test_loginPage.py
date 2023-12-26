import pytest
from pageObjects.Login import LoginPage
from utilities.readProperties import readConfig

class TestLogin:
    baseURL = readConfig.getApplicationURL()

    def setup_page(self, driver):
        driver.get(self.baseURL)
        driver.implicitly_wait(10)
        lp = LoginPage(driver)
        act_title = driver.title
        return act_title

    def test_TC_LOGIN_001(self, setup):
        self.driver = setup
        self.setup_page(self.driver)
        lp = LoginPage(self.driver)
        lp.success_login()
    def test_TC_LOGIN_002(self, setup):
        self.driver = setup
        self.setup_page(self.driver)
        lp = LoginPage(self.driver)
        lp.verify_account_not_registered()
