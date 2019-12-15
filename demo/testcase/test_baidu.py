from selenium.webdriver.common.by import By
# from demo.page import MainPage, BaiduPage
from demo.page.BaiduPage import BaiduPage
from demo.page.MainPage import MainPage



class TestBaidu():

    # _url: str = 'http://www.baidu.com'
    @classmethod
    def setup_class(cls):
        # print('setup class began')
        # _url = 'http://www.baidu.com'
        # cls.P = MainPage(_url)
        # cls.driver = BaiduPage().driver
        cls.Main = MainPage()

    # def test_tohaopage(self):
        # self.P.

    def test_bai(self):
        url = 'http://www.baidu.com'
        self.Main.to_main(url).to_haopage()
        print('abd')







