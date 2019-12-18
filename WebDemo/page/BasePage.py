import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from WebDemo.driver.TheDrivers import TheDrivers


class BasePage(object):
    _url = 'http://www.baidu.com'

    # def __init__(self):
    #     self.Drivers: WebDriver
    #     self.Drivers = TheDrivers().Drivers
    #     self.Drivers.get(self._url)
    #     self.Drivers.implicitly_wait(30)

    @classmethod
    def GetDrivers(cls):
        cls.drivers: WebDriver
        cls.drivers = TheDrivers().drivers
        cls.drivers.get(cls._url)
        cls.drivers.implicitly_wait(30)
        # self.driver.get(url)
        # self.Drivers = TheDrivers.get_driver().get(url)
        return cls.drivers

    def find(self, kv) -> WebElement:
        return self.drivers.find_element(*kv)

    

if __name__ == "__main__":
    # BasePage().GetDrivers()
    BasePage().GetDrivers
    BasePage().GetDrivers().find_element_by_xpath('//*[text()="hao123"]').click()
    # time.sleep(5)