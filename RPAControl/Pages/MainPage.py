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
        self.driver.get(self._url)
        return LoginPage()

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    b = MainPage().driver
    b.get('http://www.baidu.com')
    b.execute_script("document.body.style.zoom='0.5'")

    # a = MainPage().home()
