from selenium.webdriver.common.by import By
import time

class LoginPage:
    loginButton = 'loginBtn'
    emailTxt = 'login-email'
    passwordTxt = 'login-password'
    loginModalButton = 'login-modal-button'
    close_modal = "//i[@aria-label='Close']"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def driver_close(self):
        self.driver.close()

    def data_login(self, email, password):
        self.driver.find_element(By.XPATH, self.close_modal).click()
        self.driver.find_element(By.ID, self.loginButton).click()
        self.driver.find_element(By.ID, self.emailTxt).send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.ID, self.passwordTxt).send_keys(password)
        time.sleep(5)

    def success_login(self):
        self.data_login('pauziah@yopmail.com', 'N3ZzrLbyHKvuKwQ')
