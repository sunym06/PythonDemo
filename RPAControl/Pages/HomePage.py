import time

from selenium.webdriver.common.by import By
from RPAControl.Pages.Base import Base
from RPAControl.Pages.RobotsPage import RobotsPage
from RPAControl.Pages.RobotPage import RobotPage


class HomePage(Base):
    _RobotManger = (By.XPATH, '//span[text()="机器人管理"]')
    _robot_manger_status = (By.XPATH, '//span[text()="机器人管理"]/../..')
    _Robot = (By.XPATH, '//span[text()="机器人"]')
    _RobotGroup = (By.XPATH, '//span[text()="机器人组"]')

    def _is_open(self):
        status = False
        time.sleep(2)
        menu = self.find(self._robot_manger_status)
        if 'is-opened' in menu.get_attribute('class'):
            status = True
        print("class is :" + menu.get_attribute('class'))
        print('status is ' + str(status))
        return status

    def open_robot_manger(self):
        # self.driver.execute_script("document.body.style.zoom='0.9'")
        # self.find_ele(self._RobotManger).click()
        self.driver.execute_script('alert("aaa")')
        self.find(self._RobotManger).click()
        return self

    def to_robot(self):
        # self.find_ele(self._RobotManger).click()
        # ele = self.find_ele(self._RobotMangerStatus)
        if self._is_open():
            time.sleep(3)
            self.find(self._Robot).click()
        else:
            self.find(self._RobotManger).click()
            self.find(self._Robot).click()
        return RobotPage()

    def to_robots(self):
        print("status: " + str(self._is_open()))
        if self._is_open():
            self.find(self._RobotGroup).click()
        else:
            self.find(self._RobotManger).click()
            self.find(self._RobotGroup).click()
        return RobotsPage()




