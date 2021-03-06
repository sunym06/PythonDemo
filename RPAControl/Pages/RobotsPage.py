from selenium.webdriver.common.by import By

from RPAControl.Pages.RobotsAddPage import RobotsAddPage
from RPAControl.Pages.Base import Base


class RobotsPage(Base):
    _add = (By.XPATH, '//span[text()="新 增"]')
    _search = (By.XPATH, '//span[text()="搜 索"]')
    _clear = (By.XPATH, '//span[text()="清 空"]')
    _robotName = (By.XPATH, '//input[@placeholder="机器人组名称"]')
    _robotKind = (By.XPATH, '//input[@placeholder="机器人组类型"]')

    def add_robot(self):
        self.find(self._add).click()
        return RobotsAddPage()

    def search_robots(self, robots_name, robots_kind):
        if robots_name is not None:
            self.find(self._robotName).send_keys(robots_name)
        if robots_kind is not None:
            self.robots_kind(robots_kind)
        self.find(self._search).click()
        return self

    def clear_robot(self):
        self.find(self._clear).click()
        return self
