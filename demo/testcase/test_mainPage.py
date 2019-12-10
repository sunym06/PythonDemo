from demo.driver.ChromeDriver import ChromeDriver


class TestMainPage():

    @classmethod
    def setup_class(cls):
        cls.driver = ChromeDriver().get_drivers()