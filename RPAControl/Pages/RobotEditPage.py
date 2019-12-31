from selenium.webdriver.common.by import By
from RPAControl.Pages.Base import Base


class RobotEditPage(Base):

    _robotName = (By.XPATH, '//input[@placeholder="请输入 机器人名称"]')
    _description = (By.XPATH, '//textarea[@placeholder="请输入 描述"]')
    _edit = (By.XPATH, '//span[text()="修 改"]')
    _message = (By.XPATH, '//p[@class="el-message__content"]')

    def edit(self, robot_name="no input", robot_kind="no input", robot_description="no input"):

        if robot_name != "no input":
            self.find(self._robotName).clear()
            self.find(self._robotName).send_keys(robot_name)
        if robot_kind != "no input":
            self.select("机器人类型", robot_kind)
            self.find(self._description).clear()
        if robot_description != "no input":
            self.find(self._description).clear()
            self.find(self._description).send_keys(robot_description)
        title, key = self.assert_inner()
        self.find(self._edit).click()
        result, status = self.assert_outer(robot_name)
        return title, key, result, status

        # message = self.find(self._message).get_attribute('innerHTML')
        # return message
