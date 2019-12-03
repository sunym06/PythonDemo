from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from WebDemo.driver.ChromeDrivers import ChromeDrivers
from WebDemo.page.HaoPage import HaoPage
from WebDemo.page.PeoplePage import PeoplePage


class MainPage(object):
    _hao123 = (By.XPATH, '//a[text()="hao123"]')

    def __init__(self):
        self.drivers: WebDriver
        self.drivers = ChromeDrivers.get_driver()
        # self.drivers = ChromeDrivers.get_driver()
        # self.drivers = ChromeDrivers().get_driver()
        # self.drivers = ChromeDrivers().get_driver()
        print('make a driver')

    def to_hao123(self):
        self.drivers.find_element(By.XPATH, '//a[text()="hao123"]').click()
        print('open hao123')
        return HaoPage()

    def my_find(self, kv):
        return self.drivers.find_element(*kv)


if __name__ == "__main__":
    a = MainPage()
    a.to_hao123()
