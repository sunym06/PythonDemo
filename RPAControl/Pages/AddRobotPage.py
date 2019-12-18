import time
from datetime import datetime
from selenium.webdriver.common.by import By
from RPAControl.Pages.BasePage import BasePage
# from RPAControl.Pages.RobotPage import RobotPage


class AddRobotPage(BasePage):

    _robotName = (By.XPATH, '//input[@placeholder="请输入 机器人名称"]')
    _description = (By.XPATH, '//textarea[@placeholder="请输入 描述"]')
    _robotKind = (By.XPATH, '//input[@placeholder="请选择 机器人类型"]')
    _lis = (By.XPATH, '//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[text()="无人值守"]')
    _save = (By.XPATH, '//span[text()="保 存"]')
    _cancels = (By.XPATH, '//span[text()="取 消"]')

    def add(self, robotname, robotkind):
        times = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.find_ele(self._robotName).send_keys(times)
        self.robotkind(robotkind)
        # self.click_list(robotname, robotstatus)
        # self.find_ele(self._robotKind).click()
        # self.find_eles(self._lis)[1].click()
        self.find_ele(self._description).send_keys(times+'\n' + times + '\n' + times)
        self.find_ele(self._save).click()

        # return RobotPage()
