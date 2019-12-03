from WebDemo.page.MainPage import MainPage


class TestMain(object):


    def test_open(self):
        MainPage().open()

    def test_login(self):
        # MainPage().to_hao123().to_people()
        MainPage().to_hao123().to_people()

