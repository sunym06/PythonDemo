from WebDemo.page.BasePage import BasePage
from WebDemo.page.MainPage import MainPage


class TestMain(object):

    # def setup(self):
    #     main = MainPage()

    def test_to_people(self):
        # MainPage().to_hao123().to_people()
        MainPage().to_hao123().to_people()

    def test_to_ti1(self):
        MainPage().to_news().to_ti1()
        hands = MainPage().drivers.window_handles
        for i in hands
