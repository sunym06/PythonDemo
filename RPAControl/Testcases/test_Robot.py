import time
from datetime import datetime

import pytest

from RPAControl.Pages.MainPage import MainPage


class TestRobot(object):

    @classmethod
    def setup_class(cls):
        cls.contents_str = datetime.now().strftime('edit: \n' + '%Y-%m-%d:%H-%M-%S')

        cls.Pages = MainPage().home().login('admin', '111111')
        # cls.driver.login()

        print('\n  =========setup_class=========\n')

    def teardown_method(self):
        self.Pages.to_home()
        # return self
        print('\n  =========teardown_method=========\n')

    @pytest.mark.parametrize('robot_name, robot_kind, robot_description', [
        ('T61213', '无人值守', 'test a'),
        ('T61223', '人工参与', 'test 吧')
    ])
    def test_add_robot(self, robot_name, robot_kind, robot_description):
        self.Pages.to_robot().add_robot().add(robot_name, robot_kind, robot_description)

    @pytest.mark.parametrize('name', ['1226', 'W25'])
    def test_edit_robot(self, name):
        robot_name = self.contents_str
        robot_kind = "无人值守"
        description = 'EDIT: \n' + self.contents_str + '\n' + self.contents_str
        self.Pages.to_robot().edit_robot(name).edit(None, None, description)

    @pytest.mark.parametrize('name', ['T68'])
    def test_del_robot(self, name):
        self.Pages.to_robot().del_robot(name)

    def test_robot_search(self):
        self.Pages.to_robot().add_robot().search_robot("T619", "人工参与", "未注册")

    def test_group(self):
        self.Pages.to_robots()

    def test_robots_search(self):
        self.Pages.to_robots().search_robots("wang", "测试")

    def test_t(self):
        self.Pages.to_robot().del_robot('T617')
