from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from demo.driver.ChromeDriver import ChromeDriver


class BasePage(object):
    """
    html 页面元素基类，提供常用方法，self.driver
    """
    def __init__(self):
        self.driver = ChromeDriver().driver

    def finds(self, kv) -> WebElement:
        return self.driver.find(*kv)


if __name__ == "__main__":
    _url = 'http://www.baidu.com'
    _kw = (By.ID, 'kw')
    a = BasePage()
    a.driver.get(_url)
    a.finds(_kw).send_keys('123')
