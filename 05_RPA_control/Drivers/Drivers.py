from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Drivers(object):
    # driver: WebDriver

    def __init__(self):
        self.driver = webdriver.Chrome()


if __name__ == "__main__":
    url = 'http://www.baidu.com'
    # TODO why a 可保持浏览器打开，b运行结束后直接关闭浏览器
    a = Drivers()
    a.driver.get(url)
    # b = Drivers().driver.get(url)
