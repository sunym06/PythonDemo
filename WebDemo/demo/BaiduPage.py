from selenium.webdriver.common.by import By

from WebDemo.demo.MyDriver import MyDriver
from WebDemo.demo.NewsPage import NewsPage


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
