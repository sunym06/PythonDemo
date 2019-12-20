from selenium.webdriver.common.by import By
from RPAControl.Pages.BasePage import BasePage
# from RPAControl.Pages.RobotPage import RobotPage


class RobotEditPage(BasePage):

    _robotName = (By.XPATH, '//input[@placeholder="请输入 机器人名称"]')
    _description = (By.XPATH, '//textarea[@placeholder="请输入 描述"]')
    _robotKind = (By.XPATH, '//input[@placeholder="请选择 机器人类型"]')
    _edit = (By.XPATH, '//span[text()="修 改"]')
    _cancels = (By.XPATH, '//span[text()="取 消"]')
    _message = (By.XPATH, '//p[@class="el-message__content"]')

    def edit(self, robot_name, robot_kind, description):

        if robot_name is not None:
            self.find(self._robotName).clear()
            self.find(self._robotName).send_keys(robot_name)
        if robot_kind is not None:
            self.robot_kind(robot_kind)
            self.find(self._description).clear()
        if description is not None:
            self.find(self._description).clear()
            self.find(self._description).send_keys(description)
            self.find(self._edit).click()

        message = self.find(self._message).get_attribute('innerHTML')
        return message
