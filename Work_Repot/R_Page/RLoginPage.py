from selenium.webdriver.common.by import By

from Work_Repot.R_Page.RBasePage import RBasePage
from Work_Repot.R_Page.RHomePage import RHomePage


class RLoginPage(RBasePage):

    _user = (By.ID, 'username')
    _password = (By.ID, 'password')
    _bt_login = (By.NAME, 'reset')
    _bt_reset = (By.ID, 'btnReset')

    def login(self, user, password):
        self.find(self._user).send_keys(user)
        self.find(self._password).send_keys(password)
        self.find(self._bt_login).click()
        return RHomePage()


if __name__ == "__main__":
    a = RLoginPage()
    a.login('liuchang1', '111111')
