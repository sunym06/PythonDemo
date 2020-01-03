from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class GetDriver(object):
    driver: WebDriver

    def __init__(self) -> WebDriver:
        self.driver = webdriver.Chrome()


if __name__ == "__main__":
    url = 'http://www.baidu.com'
    a = GetDriver()
    a.driver.get(url)
