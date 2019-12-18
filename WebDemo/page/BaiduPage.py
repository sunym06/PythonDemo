from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# from WebDemo.page.BasePage import BasePage
from WebDemo.page.BasePage import BasePage
from WebDemo.page.HaoPage import HaoPage
from WebDemo.page.NewsPage import NewsPage


class BaiduPage(BasePage):
    _hao123 = (By.XPATH, '//a[text()="hao123"]')
    _news = (By.XPATH, '//a[text()="新闻"]')

    # 引用BasePage之后调用BasePage的init方法，如果MainPage重新写的话会覆盖掉init
    def __init__(self):
        self.drivers: WebDriver
        self.drivers = BasePage().GetDrivers()
        # self.Drivers = ChromeDrivers.get_driver()
        # self.Drivers = ChromeDrivers().get_driver()
        # self.Drivers = ChromeDrivers().get_driver()
        # print('make a driver')

    def to_hao123(self):
        self.drivers.find_element(*self._hao123).click()
        # self.Drivers.find_element_by_xpath('//a[text()="hao123"]').click()
        # self.Drivers.find_element(By.XPATH, '//a[text()="hao123"]').click()
        print('open hao123')
        return HaoPage()

    def to_news(self):
        self.drivers.find_element(*self._news).click()
        return NewsPage()

    def my_find(self, kv):
        return self.drivers.find_element(*kv)


if __name__ == "__main__":
    a = BaiduPage().to_hao123()
    # a.to_hao123()
