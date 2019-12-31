import random

from selenium.webdriver.common.by import By
from RPAControl.Pages.Base import Base


class RobotAddPage(Base):

    _robotName = (By.XPATH, '//input[@placeholder="请输入 机器人名称"]')
    _description = (By.XPATH, '//textarea[@placeholder="请输入 描述"]')
    _save = (By.XPATH, '//span[text()="保 存"]')

    def add(self, robot_name, robot_kind, robot_description):
        # todo 如果名称已存在，则返回提示信息
        self.find(self._robotName).send_keys(robot_name)
        self.select("机器人类型", robot_kind, dialog=True)
        self.find(self._description).send_keys(robot_description)
        title, key = self.assert_inner()
        self.find(self._save).click()
        result, status = self.assert_outer(robot_name)
        return title, key, result, status

    def cancel_robot(self):
        self.cancel()
        return self
