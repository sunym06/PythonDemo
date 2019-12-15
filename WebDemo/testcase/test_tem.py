

class TestTem():
    @classmethod
    def setup_class(cls):
        print("setup class")

    @classmethod
    def teardown_class(cls):
        print("teardown class")

    def setup_method(self):
        print('setup method')

    def teardown_method(self):
        print('teardown method')

    def test_add(self):
        print('add')

    def test_plu(self):
        print('plu')

    def test_a(self):
        print('aaa')
