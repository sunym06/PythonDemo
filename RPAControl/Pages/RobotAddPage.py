import time
from datetime import datetime
from selenium.webdriver.common.by import By
from RPAControl.Pages.BasePage import BasePage
# from RPAControl.Pages.RobotPage import RobotPage


class RobotAddPage(BasePage):

    _robotName = (By.XPATH, '//input[@placeholder="请输入 机器人名称"]')
    _description = (By.XPATH, '//textarea[@placeholder="请输入 描述"]')
    _robotKind = (By.XPATH, '//input[@placeholder="请选择 机器人类型"]')
    _save = (By.XPATH, '//span[text()="保 存"]')
    _cancels = (By.XPATH, '//span[text()="取 消"]')
    _message = (By.XPATH, '//p[@class="el-message__content"]')

    def add(self, robot_name, robot_kind, robot_description):
        self.find(self._robotName).send_keys(robot_name)
        self.robot_kind(robot_kind)
        self.find(self._description).send_keys(robot_description)
        self.find(self._save).click()
        message = self.find(self._message).get_attribute('innerHTML')
        return message


