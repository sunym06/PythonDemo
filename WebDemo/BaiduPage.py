from selenium.webdriver.common.by import By

from WebDemo.MyDriver import MyDriver
from WebDemo.NewsPage import NewsPage


class BaiduPage(object):

    _new = (By.XPATH, '//a[text()="新闻"]')

    def __init__(self):
        self.driver = MyDriver.get_drivers()

    def to_news(self):
        self.driver.find_element(By.XPATH, '//a[text()="新闻"]').click()
        return NewsPage()


if __name__ == "__main__" :
    a = BaiduPage()
    a.to_news()
