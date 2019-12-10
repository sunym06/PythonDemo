from selenium.webdriver.common.by import By
from demo.page.BasePage import BasePage
from demo.page.HaoPage import HaoPage


class BaiduPage(BasePage):
    """
    从MainPage启动后进入的页面
    """

    _hao = (By.XPATH, '//a[text()="hao123"]')
    _news = (By.XPATH,'//a[text()="新闻"]')

    def to_haopage(self):
        self.finds(self._hao).click()
        return HaoPage()

    def to_new(self):
        self.finds(self._news)
