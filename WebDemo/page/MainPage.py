from WebDemo.driver.WebDriver import WebDriver


class MainPage(object):
    app = WebDriver.get_drivers()

    @classmethod
    def open(cls):
        cls.app.find_element_by_xpath('//a[text()="名站"]').click()

