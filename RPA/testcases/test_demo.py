import time

from RPA.pages.DemoPage import DemoPage


class TestLogin(object):

    def test_login(self):
        # DemoPage.login(self, 'admin', '111111')
        # DemoPage.login('admin', '111111')
        DemoPage().login('admin', '111111')
        title = DemoPage.driver.title
        ti = DemoPage().driver.title
        assert ti == '中信自动化管理控制系统'
