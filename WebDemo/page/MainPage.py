from WebDemo.driver.WebDrivers import WebDrivers
from WebDemo.page.NewPage import NewPage


class MainPage(object):
    drivers = WebDrivers.get_drivers()

    @classmethod
    def open(cls):
        cls.drivers.find_element_by_xpath('//a[text()="名站"]').click()
        return NewPage

    def goto_news(self):
        self.drivers.find_element_by_xpath('//div[@class="navBarContainer-content"]//a[contains(text(),"新闻")]').click()
        return NewPage

