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
        self.page_operation()
        return RobotAddPage()

    def edit_robot(self, name):
        self.list_operation(name, '编 辑')
        return RobotEditPage()

    def del_robot(self, name, cancel=False):
        """
        :param name:指定删除的机器人名称
        :param cancel: 是否取消
        :return: 上一页面
        """
        if cancel:
            self.list_operation(name, '删 除', cancel=True)
        else:
            self.list_operation(name, "删 除")
        return RobotPage()

    def search_robot(self, robot_name, robot_kind):
        if robot_name is not None:
            self.find(self._robotName).send_keys(robot_name)
        if robot_kind is not None:
            self.robot_kind(robot_kind)
        self.find(self._search).click()
        return self

    def clear_robot(self):
        self.find(self._clear).click()
        return self

    def add(self, op):
        self.list_operation("新 增", )
