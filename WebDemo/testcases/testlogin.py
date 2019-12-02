from RPA_test.pages import LoginPage
import pytest


class TestLogin(object):

    def test_login(self):
        LoginPage.login('admin', '111111')
