from selenium.webdriver.chrome.webdriver import WebDriver

from WebDemo.driver.WebDrivers import WebDrivers


class NewPage(object):

    drivers: WebDriver
    drivers = WebDrivers.get_drivers()

    @classmethod
    def get_title(cls):
        return cls.drivers.find_element_by_xpath('//a[text()="国际"]').text
