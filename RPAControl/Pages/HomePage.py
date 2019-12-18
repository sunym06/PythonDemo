from selenium.webdriver.common.by import By
from RPAControl.Pages.BasePage import BasePage
from RPAControl.Pages.RobotPage import RobotPage


class HomePage(BasePage):
    _RobotManger = (By.XPATH, '//span[text()="机器人管理"]')
    _RobotMangerStatus = (By.XPATH, ('//span[text()="机器人管理"]/../..'))
    _Robot = (By.XPATH, '//span[text()="机器人"]')

    def open_robotmanger(self):
        # time.sleep(3)
        # self.find_ele(self._RobotManger).click()
        self.find_ele(self._RobotManger).click()
        return self

    def to_robot(self):
        # self.find_ele(self._RobotManger).click()
        ele = self.find_ele(self._RobotMangerStatus)
        if ele.get_attribute('class') == 'el-submenu':
            self.find_ele(self._RobotManger).click()
            self.find_ele(self._Robot).click()
        else:
            self.find_ele(self._Robot).click()
        return RobotPage()




