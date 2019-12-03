from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from WebDemo.driver.ChromeDrivers import ChromeDrivers


class PeoplePage(object):

    _login = (By.XPATH, '//a[text()="注册"]')

    def __init__(self):
        self.drivers: WebDriver
        self.drivers = ChromeDrivers().get_driver(self._url)

    def login(self):
        self.drivers.find_element_by_xpath( '//a[text()="注册"]')


if __name__ == '__main__':
    a = PeoplePage()
    a.login()