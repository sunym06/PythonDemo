from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from WebDemo.driver.ChromeDrivers import ChromeDrivers


class MainPage(object):
    _url = 'http://www.baidu.com'
    hao123 = (By.XPATH, '//a[text()="hao123"]')
    def __init__(self):
        self.drivers: WebDriver
        self.drivers = ChromeDrivers().get_driver(self._url)

    def open(self):
        self.drivers.find_element(* hao123).click()


if __name__ == "__main__":
    a = MainPage()
    a.open()
