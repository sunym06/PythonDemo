import time

from RPAControl.Pages.MainPage import MainPage


class Test_tem():

    @classmethod
    def setup_class(cls):
        cls.Pages = MainPage().home().login()
        # cls.driver.login()

        print('\n  =========setup_class=========\n')

    # def setup_method(self):
    #     self.a.home().login()
    #     return self.a

    def teardown_method(self):
        self.Pages.to_home()
        # return self
        print('\n  =========teardown_method=========\n')

    # @classmethod
    # def teardown_class(cls):
    #     cls

    def test_tem(self):
        self.Pages.to_robot()
        time.sleep(5)
        # self.driver.open_robotmanger().to_robot().add_robot()
        print('\n  =========test_tem=========\n')

    def test_b(self):
        time.sleep(3)
        self.Pages.to_robot().add_robot()
        print('\n  =========test_b=========\n')

    def test_add_robot(self):
        self.Pages.to_robot().add_robot().add()

