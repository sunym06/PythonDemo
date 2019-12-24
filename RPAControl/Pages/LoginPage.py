from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from RPAControl.Pages.BasePage import BasePage
from RPAControl.Pages.HomePage import HomePage


class LoginPage(BasePage):
    _user = (By.NAME, 'username')
    _password = (By.NAME, 'password')
    _login = (By.XPATH, '//span[text()="登录"]')

    def login(self, user=None, password=None):
        # self.driver = self.get_driver()

        self.find(self._user).clear()
        self.find(self._user).send_keys(user)
        self.find(self._password).clear()
        self.find(self._password).send_keys(password)
        self.find(self._login).click()
        return HomePage()


if __name__ == "__main__":
    a = LoginPage().login()

    # a = LoginPage().driver.find_element(By.XPATH, '//span[text()="登录"]').send_keys('admin')
