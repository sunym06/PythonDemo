from selenium.webdriver.common.by import By
from WebDemo.demo.MyDriver import MyDriver
from WebDemo.demo.TiePage import TiePage


class NewsPage(object):

    _tie = (By.XPATH, '//a[text()="贴吧"]')

    def to_tie(self):
        MyDriver.the_driver.find_element(By.XPATH, '//a[text()="贴吧"]').click()
        return TiePage()


if __name__ == "__main__" :
    a = NewsPage()
    a.to_tie()
