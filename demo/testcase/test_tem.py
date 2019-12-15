from selenium.webdriver.common.by import By

from demo.page.MainPage import MainPage


class TestT():
    _url = 'http://www.baidu.com'
    _kw = (By.ID, 'kw')

    def test_t(self):
        a = MainPage(self._url)
        a.finds(self._kw).send_keys('123')



