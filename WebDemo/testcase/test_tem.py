

class TestTem():
    @classmethod
    def setup_class(cls):
        print('\n==========setup_class=========\n')

    @classmethod
    def teardown_class(cls):
        print('\n==========teardown_class=========\n')

    def setup_method(self):
        print('\n==========setup_method=========\n')

    def teardown_method(self):
        print('\n==========teardown_method=========\n')

    def test_add(self):
        print('\n==========test_add=========\n')

    def test_plu(self):
        print('\n==========test_plu=========\n')

    def test_a(self):
        print('\n==========test_a=========\n')
