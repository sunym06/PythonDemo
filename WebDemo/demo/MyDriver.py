from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class MyDriver(object):
    url = 'http://www.baidu.com'
    the_driver: WebDriver
    @classmethod
    def get_drivers(cls):
        cls.the_driver = webdriver.Chrome()
        cls.the_driver.get(cls.url)
        return cls.the_driver


if __name__ == "__main__" :
    a = MyDriver()
    a.get_drivers()
