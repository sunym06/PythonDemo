import time

from Work_Repot.GetDriver.GetDriver import GetDriver
from Work_Repot.R_Page.RMainPage import RMainPage


class TestLogin(object):

    @classmethod
    def setup_class(cls):
        cls.login_page = RMainPage().start()

    def test_login(self):
        self.login_page.login('liuchang1', '123456')


