from datetime import datetime
import pytest
from RPAControl.Pages.MainPage import MainPage
from RPAControl.data.GetData import GetData


class TestRobot(object):

    file = r'C:\sunym\03_workspace\00_PythonWorkspac\RPAControl\data\data.xlsx'
    data = GetData(file).get_value('robot')

    @classmethod
    def setup_class(cls):
        cls.contents_str = datetime.now().strftime('edit: \n' + '%Y-%m-%d:%H-%M-%S')
        cls.Pages = MainPage().home().login('admin', '111111')
        print(cls.data)

    def teardown_method(self):
        self.Pages.to_home()

    @pytest.mark.parametrize('robot_name, robot_kind, robot_description, title, key, result, status', data)
    def test_add_robot(self, robot_name, robot_kind, robot_description, title, key, result, status):
        _title, _key, _result, _status = self.Pages.to_robot().add_robot().add(robot_name, robot_kind, robot_description)
        assert _result == result
        assert len(_key) == int(key)
        assert _title == title
        assert _status == status

    def test_add_robot_cancel(self):
        self.Pages.to_robot().add_robot().cancel_robot()

    @pytest.mark.parametrize('robot_name, robot_kind, robot_description, title, key, result, status', data)
    def test_edit_robot(self, robot_name, robot_kind, robot_description, title, key, result, status):
        _title, _key, _result, _status = self.Pages.to_robot().edit_robot(robot_name).\
            edit(robot_name=robot_name, robot_kind=robot_kind, robot_description=robot_description)
        assert _result == result
        assert len(_key) == int(key)
        assert _title == title
        assert _status == status

    @pytest.mark.parametrize('name', ['T12213'])
    def test_del_robot(self, name):
        self.Pages.to_robot().del_robot(name)

    @pytest.mark.parametrize('_robot_name, _robot_kind, _robot_status', [
        ('T2111111ab', '人工参与', '未注册'),
        ('surface', '无人值守', '空闲')
    ])
    def test_robot_search(self, _robot_name, _robot_kind, _robot_status):
        self.Pages.to_robot().search(robot_name=_robot_name, robot_kind=_robot_kind, robot_status=_robot_status )

    def test_group(self):
        self.Pages.to_robots()

    def test_robots_search(self):
        self.Pages.to_robots().search_robots("wang", "测试")



