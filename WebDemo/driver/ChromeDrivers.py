from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class ChromeDrivers(object):

    def __init__(self):
        self.driver: WebDriver
        self.driver = webdriver.Chrome()

    def get_driver(self, url):
        # self.url = url
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        return self.driver


if __name__ == "__main__":
    print("began to run ")
    urls = 'http://www.baidu.com'
    a = ChromeDrivers()
    a.get_driver(urls)
    # a = ChromeDrivers(url).get_driver()
