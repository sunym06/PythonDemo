from WebDemo.page.BasePage import BasePage
from WebDemo.page.BaiduPage import BaiduPage
import pytest


class TestMain(object):

    # def setup(self):
    #     main = MainPage()
    @classmethod
    def setup_class(cls):
        print("setup class")

    @classmethod
    def teardown_class(self):
        print("teardown class")

    def teardown_method(self):
        print('began to teardown')

    def test_to_people(self):
        # MainPage().to_hao123().to_people()
        BaiduPage().to_hao123().to_people()

    def test_to_people2(self):
        # MainPage().to_hao123().to_people()
        BaiduPage().to_hao123()



    # def test_to_ti1(self):
    #     MainPage().to_news().to_ti1()
    #     hands = MainPage().drivers.window_handles
    #     for i in hands
