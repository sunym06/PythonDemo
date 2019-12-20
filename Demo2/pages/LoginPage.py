from selenium.webdriver.common.by import By
from Demo2.pages.BasePage import BasePage


class LoginPage(BasePage):
    _user = (By.NAME, 'username')
    _password = (By.NAME, 'password')
    _loginbutton = (By.XPATH, '//span[contains(text()," 登录")]')

    def login(self):
        self.driver.find(*self._user).send_keys('admin')
        self.driver.find(*self._password).send_keys('111111')
        self.driver.find(*self._loginbutton).click()


if __name__ == "__main__":
    # a = LoginPage().login()
    a = main().login()
