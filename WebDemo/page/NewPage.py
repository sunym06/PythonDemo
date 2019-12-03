from selenium.webdriver.chrome.webdriver import WebDriver

from WebDemo.driver.ChromeDrivers import ChromeDrivers


class NewPage(object):

    drivers: WebDriver
    drivers = ChromeDrivers.get_drivers()

    # @classmethod
    def get_title(self):
        return self.drivers.find_element_by_xpath('//a[text()="国际"]').text
