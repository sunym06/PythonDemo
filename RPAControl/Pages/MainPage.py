import time

from selenium.webdriver.chrome.webdriver import WebDriver
from RPAControl.Drivers.ChromeDrivers import ChromeDrivers
from RPAControl.Pages.BasePage import BasePage
from RPAControl.Pages.LoginPage import LoginPage


class MainPage(BasePage):

    _url = 'http://192.168.8.222:8111/#/wel/index'
    _url2 = 'http://111.231.110.64:8222/#/wel/index'
    driver: WebDriver

    def home(self):
        self.driver.get(self._url2)
        return LoginPage()

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    b = MainPage().driver
    b.get('https://www.baidu.com/')

    def login(kw=None):
        b.find_element_by_id('kw').send_keys(kw)
    login()
    # a = MainPage().home()
