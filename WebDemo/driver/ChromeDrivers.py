from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class ChromeDrivers(object):

    driver: WebDriver

    @classmethod
    def get_driver(cls):
        cls.driver = webdriver.Chrome()
        url = 'http://www.baidu.com'
        cls.driver.implicitly_wait(30)
        cls.driver.get(url)
        return cls.driver


if __name__ == "__main__":
    print("began to run ")
    a = ChromeDrivers()
    a.get_driver()
    # a = ChromeDrivers(url).get_driver()
