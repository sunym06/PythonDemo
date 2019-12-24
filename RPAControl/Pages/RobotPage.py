from selenium.webdriver.common.by import By

from RPAControl.Pages.RobotAddPage import RobotAddPage
from RPAControl.Pages.BasePage import BasePage
from RPAControl.Pages.RobotEditPage import RobotEditPage


class RobotPage(BasePage):
    _add = (By.XPATH, '//span[text()="新 增"]')
    _search = (By.XPATH, '//span[text()="搜 索"]')
    _clear = (By.XPATH, '//span[text()="清 空"]')
    _robotName = (By.XPATH, '//input[@placeholder="机器人名称"]')
    _robotKind = (By.XPATH, '//input[@placeholder="机器人类型"]')

    def add_robot(self):
        self.find(self._add).click()
        return RobotAddPage()

    def edit_robot(self, name):
        self.list_option(name, '编 辑')
        return RobotEditPage()

    def del_robot(self, name):
        self.list_option(name, '删 除')
        self.cancel()
        return RobotPage()

    def search_robot(self, robotname, robotkind):
        if robotname is not None:
            self.find(self._robotName).send_keys(robotname)
        if robotkind is not None:
            self.robot_kind(robotkind)
        self.find(self._search).click()
        return self

    def clear_robot(self):
        self.find(self._clear).click()
        return self

