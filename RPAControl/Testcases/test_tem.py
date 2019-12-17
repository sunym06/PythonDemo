from RPAControl.Pages.MainPage import MainPage


class Test_tem():
    # @classmethod
    # def setup_class(cls):
    #     cls.
    def setup_method(self):
        self.a = MainPage()
        return self.a

    def teardown_method(self):
        self.a.close()

    def test_tem(self):
        self.a.home().login().to_robotmanger()
        # a.login().to_robotmanger()

    def test_b(self):
        # b = MainPage().home().login().to_robotmanger()
        self.a.home().login().to_robotmanger()
