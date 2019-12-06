from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class TheDrivers(object):

    driver: WebDriver

    def __init__(self):
        self.drivers = webdriver.Chrome()

    # @classmethod
    # def get_driver(cls):
    #     pass
    #     # 打开一个空Chrome
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.implicitly_wait(30)
    #     url = 'http://www.baidu.com'
    #     cls.driver.get(cls.url)
    #     return cls.driver


if __name__ == "__main__":
    print("began to run ")
    a = TheDrivers()

    # a = ChromeDrivers(url).get_driver()
