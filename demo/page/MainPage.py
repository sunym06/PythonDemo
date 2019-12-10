from selenium.webdriver.common.by import By
from demo.page.BaiduPage import BaiduPage
from demo.page.BasePage import BasePage
from demo.page.HaoPage import HaoPage


class MainPage(BasePage):
    """
    入口页面，跳转至指定URL页面
    """

    # def __init__(self):
    #     BasePage.__init__(self)
        # self.driver.get(url)
        # self.finds(self._hao)

    def to_main(self, url):
        self.driver.get(url)
        return BaiduPage()
    # def start(self, url):

    # def start(self):
    #     self.driver.get(self._url)
    #     return 'nothing'

    # def finds(self, kv):
    #     self.driver.find_element(*kv)
    #
    # def toHaoPage(self):


if __name__ == "__main__":
    _url = 'http://www.baidu.com'
    _kw = (By.ID, 'kw')
    a = MainPage(_url)
    a.finds(_kw).send_keys('123')

