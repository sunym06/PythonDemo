from selenium.webdriver.common.by import By
from WebDemo.page.BasePage import BasePage


class PeoplePage(BasePage):

    _login = (By.XPATH, '//a[text()="注册"]')

    # def __init__(self):
    #     self.Drivers: WebDriver
    #     self.Drivers = TheDrivers().get_driver(self._url)

    def login(self):
        self.drivers.find_element_by_xpath( '//a[text()="注册"]')


if __name__ == '__main__':
    a = PeoplePage()
    a.login()
