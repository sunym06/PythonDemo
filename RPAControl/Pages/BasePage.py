import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from RPAControl.Drivers.ChromeDrivers import ChromeDrivers


class BasePage(object):

    driver: WebDriver
    driver = ChromeDrivers.get_driver()

    def find_ele(self,  kv) -> WebElement:
        for i in range(5):
            ele = self.driver.find_element(*kv)
        return ele

    def find_eles(self,  kv) -> list:
        time.sleep(2)
        for i in range(5):
            eles = self.driver.find_elements(*kv)
        return eles

    def click_list(self, parameter, val):
        _robotKind = (By.XPATH, '//input[@placeholder={}]'.format(parameter))
        _lis = (By.XPATH,
                '//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[text()={}]'.format(val))
        self.find_ele(self._robotKind).click()
        time.sleep(2)
        if len(self.find_eles(self._lis)) >1:
            self.find_eles(self._lis)[1].click()
        else:
            self.find_ele(self._lis).click()

    def robotkind(self, robotkind):
        _robotKind = (By.XPATH, '//input[contains(@placeholder,"机器人类型")]')
        _lis = (By.XPATH,
                '//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[text()="{}"]'.format(
                    robotkind))
        self.find_eles(_robotKind)[-1].click()
        self.find_eles(_lis)[-1].click()


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