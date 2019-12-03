from WebDemo.page.MainPage import MainPage
import pytest


class TestMain(object):

    def test_open(self):
        MainPage.open()

