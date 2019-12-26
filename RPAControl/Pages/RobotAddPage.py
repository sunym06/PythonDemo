import time
from datetime import datetime
from selenium.webdriver.common.by import By
from RPAControl.Pages.Base import Base
# from RPAControl.Pages.RobotPage import RobotPage


class RobotAddPage(Base):

    _robotName = (By.XPATH, '//input[@placeholder="请输入 机器人名称"]')
    _description = (By.XPATH, '//textarea[@placeholder="请输入 描述"]')
    _robotKind = (By.XPATH, '//input[@placeholder="请选择 机器人类型"]')
    _save = (By.XPATH, '//span[text()="保 存"]')
    _cancels = (By.XPATH, '//span[text()="取 消"]')
    _message = (By.XPATH, '//p[@class="el-message__content"]')

    def add(self, robot_name, robot_kind, robot_description):
        _name = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[text()="{}"]/../../../..//span[text()="{}"]')
        _status = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[text()="{}"]/../../../../'
                             'td[contains(@class,"column_8")]'.format(robot_name))
        # todo 如果名称已存在，则返回提示信息
        self.find(self._robotName).send_keys(robot_name)
        self.select("机器人类型", robot_kind, dialog=True)
        self.find(self._description).send_keys(robot_description)
        self.find(self._save).click()
        status = self.find(_status).get_attribute('textContent')
        message = self.find(self._message).get_attribute('innerHTML')
        return status, message

