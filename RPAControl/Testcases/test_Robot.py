import time
from datetime import datetime

from RPAControl.Pages.MainPage import MainPage


class TestRobot(object):

    @classmethod
    def setup_class(cls):
        cls.Pages = MainPage().home().login()
        # cls.driver.login()

        print('\n  =========setup_class=========\n')

    def teardown_method(self):
        self.Pages.to_home()
        # return self
        print('\n  =========teardown_method=========\n')

    def test_add_robot(self):
        robot_name = "test"
        robot_kind = '无人值守'
        robot_description = ""
        self.Pages.to_robot().add_robot().add(robot_name, robot_kind, robot_description)

    def test_edit_robot(self):
        contents = datetime.now().strftime('edit: \n' + '%Y-%m-%d:%H-%M-%S')
        robot_name = '2019-12-19:12-43-10'
        robot_kind = "无人值守"
        description = 'EDIT: \n' + contents + '\n' + contents
        self.Pages.to_robot().edit_robot(robot_name).edit(contents, robot_kind, description)

    def test_del_robot(self, cancel=True):
        name = '2019-12-19:12-56-14'
        self.Pages.to_robot().del_robot(name)

    def test_robot_search(self):
        self.Pages.to_robot().search_robot("", "无人值守")

    def test_group(self):
        self.Pages.to_robots()

    def test_robots_search(self):
        self.Pages.to_robots().search_robots("wang", "测试")

