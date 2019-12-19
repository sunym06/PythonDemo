import time

from selenium.webdriver.common.by import By
from RPAControl.Pages.BasePage import BasePage
from RPAControl.Pages.RobotsPage import RobotsPage
from RPAControl.Pages.RobotPage import RobotPage


class HomePage(BasePage):
    _RobotManger = (By.XPATH, '//span[text()="机器人管理"]')
    _robot_manger_status = (By.XPATH, '//span[text()="机器人管理"]/../..')
    _Robot = (By.XPATH, '//span[text()="机器人"]')
    _RobotGroup = (By.XPATH, '//span[text()="机器人组"]')

    def _is_open(self):
        status = False
        time.sleep(2)
        ele = self.find_ele(self._robot_manger_status)
        if 'is-opened' in ele.get_attribute('class'):
            status = True
        print("class is :" + ele.get_attribute('class'))
        print('status is ' + str(status))
        return status

    def open_robot_manger(self):
        # time.sleep(3)
        # self.find_ele(self._RobotManger).click()
        self.find_ele(self._RobotManger).click()
        return self

    def to_robot(self):
        # self.find_ele(self._RobotManger).click()
        # ele = self.find_ele(self._RobotMangerStatus)
        if self._is_open():
            self.find_ele(self._Robot).click()
        else:
            self.find_ele(self._RobotManger).click()
            self.find_ele(self._Robot).click()
        return RobotPage()

    def to_robots(self):
        print("status: " + str(self._is_open()))
        if self._is_open():
            self.find_ele(self._RobotGroup).click()
        else:
            self.find_ele(self._RobotManger).click()
            self.find_ele(self._RobotGroup).click()
        return RobotsPage()




