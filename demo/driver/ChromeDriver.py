from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class ChromeDriver(object):
    """基本信息
    生成基本driver
    """
    def __init__(self) -> WebElement:
        self.driver = webdriver.Chrome()

    def get_drivers(self):
        return self.driver


if __name__ == "__main__":
    a = ChromeDriver()
