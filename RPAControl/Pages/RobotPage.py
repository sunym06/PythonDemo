from selenium.webdriver.common.by import By

from RPAControl.Pages.CommonPages import CommonPages
from RPAControl.Pages.RobotAddPage import RobotAddPage
from RPAControl.Pages.Base import Base
from RPAControl.Pages.RobotEditPage import RobotEditPage


class RobotPage(CommonPages):
    _robotName = (By.XPATH, '//input[@placeholder="机器人名称"]')
    _robotKind = (By.XPATH, '//input[@placeholder="机器人类型"]')

    def add_robot(self):
        self.add()
        # self.page_operation()
        return RobotAddPage()

    def clear_robot(self):
        self.page_operation("清 空")
        return self

    def search_robot(self, robot_name, robot_kind, robot_status):
        self.search(robot_name, robot_kind, robot_status)
        return self

    # def search_robot(self, robot_name, robot_kind, robot_status):
    #     if robot_name is not None:
    #         self.find(self._robotName).send_keys(robot_name)
    #     if robot_kind is not None:
    #         self.select("机器人类型", robot_kind, dialog=False)
    #     if robot_status is not None:
    #         self.select("机器人状态", robot_status, dialog=False)
    #     self.page_operation("搜 索")
    #     return self

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



