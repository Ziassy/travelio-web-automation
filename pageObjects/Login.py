from selenium.webdriver.common.by import By
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen
import time

class LoginPage:

    rc = readConfig

    logger = LogGen.loggen()

    loginButton = 'loginBtn'
    emailTxt = 'login-email'
    passwordTxt = 'login-password'
    loginModalButton = 'login-modal-btn'
    close_modal = '//i[@aria-label="Close"]'
    userOptionDrp = 'user-option'
    daftarPropertyButton = '//a[contains(.,"Daftarkan Properti Saya")]'
    errorMessageTxt = 'modal-error-message'
    buttonOkModalError = '//button[contains(.,"OK")]'

    messageAccountNotRegistered = 'Email atau password salah'

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
        self.driver.find_element(By.ID, self.loginModalButton).click()
        self.logger.info('************* Done input data login ***************')

    def success_login(self):
        self.data_login(self.rc.getEmail(), self.rc.getPassword())
        time.sleep(1)
        user_option = self.driver.find_element(By.ID, self.userOptionDrp).is_displayed()
        daftar_property = self.driver.find_element(By.XPATH, self.daftarPropertyButton).is_displayed()
        if user_option and daftar_property == True:
            self.driver.save_screenshot(".\\Screenshots\\success\\LOGIN-001.png")
            self.logger.info('************* capture success login LOGIN-001  ***************')
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\failed\\LOGIN-001.png")
            self.logger.info('************* capture failed login LOGIN-001  ***************')
            self.driver.close()
            assert False

    def verify_account_not_registered(self):
        self.data_login(self.rc.getUnregisteredEmail(), self.rc.getrandomPassword())
        time.sleep(1)
        error_message = self.driver.find_element(By.ID, self.errorMessageTxt).get_attribute('innerHTML')
        if error_message == self.messageAccountNotRegistered:
            self.driver.save_screenshot(".\\Screenshots\\success\\LOGIN-002.png")
            self.driver.find_element(By.XPATH, self.buttonOkModalError).click()
            self.logger.info('************* capture success verify_account_not_registered LOGIN-002  ***************')
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\failed\\LOGIN-002.png")
            self.logger.info('************* capture fail verify_account_not_registered LOGIN-002 ***************')
            self.driver.close()
            assert False



