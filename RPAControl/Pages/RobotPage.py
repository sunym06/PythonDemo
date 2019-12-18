from selenium.webdriver.common.by import By

from RPAControl.Pages.AddRobotPage import AddRobotPage
from RPAControl.Pages.BasePage import BasePage


class RobotPage(BasePage):
    _add = (By.XPATH, '//span[text()="新 增"]')
    _search = (By.XPATH, '//span[text()="搜 索"]')
    _clear = (By.XPATH, '//span[text()="清 空"]')

    def add_robot(self):
        self.find_ele(self._add).click()
        return AddRobotPage()

    def search_robot(self):
        self.find_ele(self._search).click()
        return self

    def clear_robot(self):
        self.find_ele(self._clear).click()
        return self
