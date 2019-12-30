import time
from datetime import datetime

import pytest

from RPAControl.Pages.MainPage import MainPage


class TestRobot(object):

    @classmethod
    def setup_class(cls):
        cls.contents_str = datetime.now().strftime('edit: \n' + '%Y-%m-%d:%H-%M-%S')
        cls.Pages = MainPage().home().login('admin', '111111')

    def teardown_method(self):
        self.Pages.to_home()

    @pytest.mark.parametrize('robot_name, robot_kind, robot_description, title, key, result, status', [
        ('T2111111aa', '无人值守', 'test a', "新 增", 32, "操作成功!", "未注册"),
        ('T2111111ab', '人工参与', 'test b', "新 增", 32, "操作成功!", "未注册")
    ])
    def test_add_robot(self, robot_name, robot_kind, robot_description, title, key, result, status):
        _title, _key, _result, _status = self.Pages.to_robot().add_robot().add(robot_name, robot_kind, robot_description)
        assert _result == result
        assert len(_key) == 32
        assert _title == "新 增"
        assert _status == status

    def test_add_robot_cancel(self):
        for i in range(5):
            self.Pages.to_robot().add_robot().cancel_robot()

    @pytest.mark.parametrize('name', ['T12a1bc', 'T12213'])
    def test_edit_robot(self, name):
        robot_name = self.contents_str
        robot_kind = "无人值守"
        descriptions = 'EDIT: \n' + self.contents_str + '\n' + self.contents_str
        self.Pages.to_robot().edit_robot(name).edit(robot_kind=robot_kind, description=descriptions)

    @pytest.mark.parametrize('name', ['T12213'])
    def test_del_robot(self, name):
        self.Pages.to_robot().del_robot(name)

    def test_robot_search(self):
        self.Pages.to_robot().search(robot_kind="人工参与", robot_status="未注册")

    def test_group(self):
        self.Pages.to_robots()

    def test_robots_search(self):
        self.Pages.to_robots().search_robots("wang", "测试")
