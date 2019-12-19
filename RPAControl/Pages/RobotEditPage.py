from datetime import datetime
from selenium.webdriver.common.by import By
from RPAControl.Pages.BasePage import BasePage
# from RPAControl.Pages.RobotPage import RobotPage


class RobotEditPage(BasePage):

    _robotName = (By.XPATH, '//input[@placeholder="请输入 机器人名称"]')
    _description = (By.XPATH, '//textarea[@placeholder="请输入 描述"]')
    _robotKind = (By.XPATH, '//input[@placeholder="请选择 机器人类型"]')
    _edit = (By.XPATH, '//span[text()="修 改"]')
    _cancels = (By.XPATH, '//span[text()="取 消"]')

    def edit(self, robot_name, robot_kind, description):
        self.find_ele(self._robotName).clear()
        self.find_ele(self._robotName).send_keys(robot_name)
        self.robot_kind(robot_kind)
        self.find_ele(self._description).clear()
        self.find_ele(self._description).send_keys(description)
        self.find_ele(self._edit).click()
