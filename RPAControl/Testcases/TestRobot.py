import time
from datetime import datetime

from RPAControl.Pages.MainPage import MainPage


class TestRobot(object):

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

    def test_tem(self):
        self.Pages.to_robot()

    def test_b(self):
        self.Pages.to_robot().add_robot()

    def test_add_robot(self):
        time.sleep(3)
        self.Pages.to_robot().add_robot().edit('', '无人值守')

    def test_edit_robot(self):
        name = '2019-12-19:12-45-41'
        times = datetime.now().strftime('edit: \n' + '%Y-%m-%d:%H-%M-%S')
        robot_kind = '人工参与'
        description = 'EDIT: \n' + times + '\n' + times
        self.Pages.to_robot().edit_robot(name).edit(times, robot_kind, description)

    def test_del_robot(self, cancel=True):
        name = '2019-12-19:12-56-14'
        self.Pages.to_robot().del_robot(name)

    def test_robot_search(self):
        self.Pages.to_robot().search_robot("", "无人值守")

    def test_group(self):
        self.Pages.to_robots()

    def test_robots_search(self):
        self.Pages.to_robots().search_robots("wang", "测试")

