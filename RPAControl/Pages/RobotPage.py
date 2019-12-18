import time

from selenium.webdriver.common.by import By

from RPAControl.Pages.AddRobotPage import AddRobotPage
from RPAControl.Pages.BasePage import BasePage


class RobotPage(BasePage):
    _add = (By.XPATH, '//span[text()="新 增"]')
    _search = (By.XPATH, '//span[text()="搜 索"]')
    _clear = (By.XPATH, '//span[text()="清 空"]')
    _robotName = (By.XPATH, '//input[@placeholder="机器人名称"]')
    _robotKind = (By.XPATH, '//input[@placeholder="机器人类型"]')
    _lis = (By.XPATH, '//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[text()="无人值守"]')


    def add_robot(self):
        self.find_ele(self._add).click()
        return AddRobotPage()

    def search_robot(self, robotname, robotkind):
        if robotname != "":
            self.find_ele(self._robotName).send_keys(robotname)
        if robotkind != "":
            # self.find_ele(self._robotKind).click()
            # time.sleep(1)
            # self.find_ele(self._lis).click()
            # self.click_list('请选择 机器人类型', '无人值守')
            self.robotkind(robotkind)
        self.find_ele(self._search).click()
        return self

    def clear_robot(self):
        self.find_ele(self._clear).click()
        return self
