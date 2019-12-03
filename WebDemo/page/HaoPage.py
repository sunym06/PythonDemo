from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from WebDemo.driver.ChromeDrivers import ChromeDrivers


class HaoPage(object):
    _pepole = (By.XPATH, '//a[text()="人民网"]')

    def __init__(self):
        pass

    def to_people(self):
        # drivers = ChromeDrivers.get_driver()
        # self.drivers.find_element((By.XPATH, '//a[text()="人民网"]')).click()
        # .get_driver().find_element((By.XPATH, '//a[text()="人民网"]')).click()
        # self.drivers.find_element(By.XPATH, '//a[text()="人民网"]').click()
        #
        ChromeDrivers.driver.find_element(By.XPATH, '//a[text()="人民网"]').click()
        # ChromeDrivers.get_driver().find_element(By.XPATH, '//a[text()="人民网"]').click()



