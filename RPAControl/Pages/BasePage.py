import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from RPAControl.Drivers.ChromeDrivers import ChromeDrivers


class BasePage(object):

    driver: WebDriver
    driver = ChromeDrivers.get_driver()


    def find_ele(self,  kv) -> WebElement:
        for i in range(10):
            ele = self.driver.find_element(*kv)
        return ele

    def find_eles(self,  kv) -> WebElement:
        time.sleep(2)
        for i in range(10):
            eles = self.driver.find_elements(*kv)
        return eles

    def to_home(self):
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        return self






if __name__ == "__main__":
    _url = 'http://www.baidu.com'
    # b = BasePage()
    # b.get_driver().find_element(By.ID, 'kw').send_keys('123')
    # b.find_element(By.ID, 'kw').send_keys('123')
    driver = BasePage().driver
    # driver.get(_url)
    # driver.find_element(By.ID, 'kw').send_keys('123')
    # BasePage.get_driver().find_element(By.ID, 'kw').send_keys('123')
    print(dir(driver))