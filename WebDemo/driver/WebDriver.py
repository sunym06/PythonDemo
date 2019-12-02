from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class WebDriver(object):
    url = 'https://m.sohu.com/limit/'
    driver: WebDriver
    @classmethod
    def get_drivers(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.url)
        return cls.driver
