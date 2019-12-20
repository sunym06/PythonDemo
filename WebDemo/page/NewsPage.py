from selenium.webdriver.common.by import By

from WebDemo.page.BasePage import BasePage


class NewsPage(BasePage):
    _title1 = (By.XPATH, '//li[@class="hdline2"]')

    def to_ti1(self):
        self.drivers.find(*self._title1).click()




