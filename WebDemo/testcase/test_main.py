from WebDemo.page.MainPage import MainPage


class TestMain(object):

    def test_open(self):
        MainPage().open()

    def test_intel(self):
        title = MainPage.open()
        # assert title == "国际"
