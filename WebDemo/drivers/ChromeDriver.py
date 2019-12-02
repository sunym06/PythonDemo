from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class ChromeDriver(object):
    url = 'http://192.168.9.35:1888/#/login'
    url1 = 'http://192.168.9.36:1888/#/login'
    driver: WebDriver

    @classmethod
    def get_driver(cls) -> WebDriver:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.get(cls.url1)
        return cls.driver




