from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from 05_RPA_control.Drivers.driver


class BasePage(object):
    """
    为页面对象的基础，后续页面可通过集成该类来完成具体定义
    """
    driver: WebDriver

    # def __init__(self):
    #     self.driver = Drivers().

    @classmethod
    def getDivers(cls):
        cls.driver = Drivers()

    def find(self, kv):
        for i in range(3):
            self.driver.find_element(*kv)
