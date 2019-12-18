from Demo2.drivers.Drivers import Drivers
from Demo2.pages.MainPage import MainPage


class TestNews():

    # @classmethod
    # def setup_class(cls):
    #     cls.driver = Drivers().driver

    # def setup_method(self):
    #     MainPage().main()

    def test_to_news(self):
        MainPage().main().to_news()