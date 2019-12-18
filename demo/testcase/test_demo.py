from demo.driver.ChromeDriver import ChromeDriver
from demo.page.MainPage import MainPage


class TestBaidu():

    url = 'http://www.baidu.com'
    @classmethod
    def setup_class(cls):
        cls.driver = ChromeDriver().driver

    def setup_method(self):
       pass

    def teardown_class(self):
        pass

    def teardown_method(self):
        pass

    def test_tonewspage(self):
        MainPage().main(self.url)
        # self.driver = ChromeDriver().driver
        self.driver
        url = 'http://www.baidu.com'

        self.driver.get(url)
