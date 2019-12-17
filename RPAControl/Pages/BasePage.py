from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from RPAControl.Drivers.ChromeDrivers import ChromeDrivers


class BasePage(object):

    driver: WebDriver
    driver = ChromeDrivers.get_driver()

    # def __init__(self):
    #     self.driver = ChromeDrivers().get_driver()
    # 通过 classmethod， 修饰符对应的函数不需要实例化
    # @classmethod
    # def get_driver(cls):
    #     cls.driver = ChromeDrivers().driver
    #     # cls.driver.get(cls._url)
    #     return cls.driver
    def find_ele(self,  kv) -> WebElement:
        for i in range(10):
            ele = self.driver.find_element(*kv)
        return ele

if __name__ == "__main__":
    _url = 'http://www.baidu.com'
    # b = BasePage()
    # b.get_driver().find_element(By.ID, 'kw').send_keys('123')
    # b.find_element(By.ID, 'kw').send_keys('123')
    driver = BasePage().driver
    # driver.get(_url)
    # driver.find_element(By.ID, 'kw').send_keys('123')
    # BasePage.get_driver().find_element(By.ID, 'kw').send_keys('123')
    print(dir(driver))