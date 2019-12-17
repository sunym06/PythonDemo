import time

from selenium.webdriver.common.by import By
from RPAControl.Pages.BasePage import BasePage


class HomePage(BasePage):
    _RobotManger = (By.XPATH, '//span[text()="机器人管理"]')
    _Robot = (By.XPATH, '//span[text()="机器人"]')
    _add = (By.XPATH, '//span[text()="新 增"]')

    def to_robotmanger(self):
        # time.sleep(3)
        # self.find_ele(self._RobotManger).click()
        self.find_ele(self._RobotManger).click()
        self.find_ele(self._Robot).click()
        self.find_ele(self._add).click()
