from WebDemo.page.BasePage import BasePage
from WebDemo.page.BaiduPage import BaiduPage
import pytest


class TestMain(object):

    # def setup(self):
    #     main = MainPage()
    @classmethod
    def setup_class(cls):
        print("setup class")
        cls.main = BaiduPage()

    @classmethod
    def teardown_class(self):
        print("teardown class")

    def teardown_method(self):
        print('began to teardown')

    def test_to_people(self):
        # MainPage().to_hao123().to_people()
        self.main.to_hao123().to_people()

    def test_to_people2(self):
        # MainPage().to_hao123().to_people()
        self.main.to_hao123()



    # def test_to_ti1(self):
    #     MainPage().to_news().to_ti1()
    #     hands = MainPage().Drivers.window_handles
    #     for i in hands
