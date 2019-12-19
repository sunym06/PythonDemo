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
        self.find_ele(self._add).click()
        return RobotAddPage()

    def edit_robot(self, name):
        _name = (By.XPATH, '//span[text()="{}"]/../../../..//span[text()="编 辑"]'.format(name))
        print(_name)
        self.find_elements(_name)[-1].click()
        return RobotEditPage()

    def del_robot(self, name, cancel=False):
        _name = (By.XPATH, '//span[text()="{}"]/../../../..//span[text()="删 除"]'.format(name))
        _del = (By.XPATH, '//span[contains(text(),"确定")]')
        _cancel = (By.XPATH, '//span[contains(text(),"确定")]')
        print("_name: " + '//span[text()="{}"]/../../../..//span[text()="删 除"]'.format(name))
        self.find_elements(_name)[-1].click()
        if cancel:
            self.find_ele(_cancel)
        else:
            self.find_ele(_del)
        return RobotPage()

    def search_robot(self, robotname, robotkind):
        if robotname != "":
            self.find_ele(self._robotName).send_keys(robotname)
        if robotkind != "":
            # self.find_ele(self._robotKind).click()
            # time.sleep(1)
            # self.find_ele(self._lis).click()
            # self.click_list('请选择 机器人类型', '无人值守')
            self.robot_kind(robotkind)
        self.find_ele(self._search).click()
        return self

    def clear_robot(self):
        self.find_ele(self._clear).click()
        return self
