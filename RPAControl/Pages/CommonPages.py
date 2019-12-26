from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from RPAControl.Pages.Base import Base


class CommonPages(Base):

    def common_operation(self, name):
        _name = (By.XPATH, '//span[text()= "{}"]'.format(name))
        self.find(_name).click()

    def add(self):
        self.common_operation("新 增")

    def imports(self):
        self.common_operation("导 入")

    def search(self, robot_name='no input', robot_kind='no input', robot_status='no input'):
        _id = '//input[contains(@placeholder,"ID")]'
        _robotName = (By.XPATH, '//input[@placeholder="机器人名称"]')
        _robotKind = (By.XPATH, '//input[@placeholder="机器人类型"]')
        _robot_status = (By.XPATH, '//input[@placeholder="机器人状态"]')

        if robot_name != "no input":
            self.find(self._robotName).send_keys(robot_name)
        if robot_kind != "no input":
            self.select("机器人类型", robot_kind, dialog=False)
        if robot_status != "no input":
            self.select("机器人状态", robot_status, dialog=False)

        self.common_operation("搜 索")
        return self

    def clear(self):
        self.search(robot_name='a', robot_status=2)
        self.common_operation("清 空")

    def list_operation(self, name, option, cancel=False) -> WebElement:
        _name = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[text()="{}"]/../../../..//span[text()="{}"]'
                 .format(name, option))
        _del = (By.XPATH, '//span[contains(text(),"确定")]')
        _cancel = (By.XPATH, '//span[contains(text(),"取消")]')
        try:
            ele = self.find(_name)
            ele.click()
        except:
            self.scroll(800)
            ele = self.find(_name).click()

            # todo 需要灵活滚动
            # try:
            #     self.scroll(800)
            #     ele = self.find(_name).click()
            # except:
            #     self.scroll(-800)
            #     ele = self.find(_name).click()
        # if cancel:
        #     self.find(_cancel).click()
        # else:
        #     self.find(_del).click()
        # todo return 为Element不合适
        return ele

