from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from RPAControl.Pages.BasePage import BasePage
from RPAControl.Pages.HomePage import HomePage


class LoginPage(BasePage):
    _user = (By.NAME, 'username')
    _password = (By.NAME, 'password')
    _login = (By.XPATH, '//span[text()="登录"]')
    # driver: WebDriver
    # def __init__(self):
    #     pass

    def login(self):
        # self.driver = self.get_driver()
        self.driver.find_element(*self._user).clear()
        self.driver.find_element(*self._user).send_keys('admin')
        self.driver.find_element(*self._password).clear()
        self.driver.find_element(*self._password).send_keys('111111')
        self.driver.find_element(*self._login).click()
        return HomePage()


# if __name__ == "__main__":
    # a = LoginPage().login()

    # a = LoginPage().driver.find_element(By.XPATH, '//span[text()="登录"]').send_keys('admin')
