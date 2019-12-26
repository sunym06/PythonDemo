from selenium.webdriver.common.by import By
from RPAControl.Pages.Base import Base


class RobotEditPage(Base):

    _robotName = (By.XPATH, '//input[@placeholder="请输入 机器人名称"]')
    _description = (By.XPATH, '//textarea[@placeholder="请输入 描述"]')
    _robotKind = (By.XPATH, '//input[@placeholder="请选择 机器人类型"]')
    _edit = (By.XPATH, '//span[text()="修 改"]')
    _cancels = (By.XPATH, '//span[text()="取 消"]')
    _message = (By.XPATH, '//p[@class="el-message__content"]')

    def edit(self, robot_name="no input", robot_kind="no input", description="no input"):

        if robot_name != "no input":
            self.find(self._robotName).clear()
            self.find(self._robotName).send_keys(robot_name)
        if robot_kind != "no input":
            self.select("机器人类型", robot_kind)
            # self.robot_kind(robot_kind)
            self.find(self._description).clear()
        if description != "no input":
            self.find(self._description).clear()
            self.find(self._description).send_keys(description)
            self.find(self._edit).click()

        message = self.find(self._message).get_attribute('innerHTML')
        return message
