from RPA.pages.LoginPage import LoginPage


class TestLogin(object):

    def test_login(self):
        LoginPage.login('admin', '111111')

