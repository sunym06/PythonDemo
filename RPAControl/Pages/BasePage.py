import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from RPAControl.Drivers.ChromeDrivers import ChromeDrivers


class BasePage(object):

    driver: WebDriver
    driver = ChromeDrivers.get_driver()

    def find(self, by, value) -> WebElement:
        try:
            for i in range(3):
                ele = self.driver.find_element(By.by)
            return ele
        except NoSuchElementException as e:
            print("找不到以下元素:" + print(*value))

    def finds(self, kv) -> list:
        # time.sleep(1)
        for i in range(3):
            elements = self.driver.find_elements(*kv)
        return elements

    def click_list(self, parameter, val):
        _robotKind = (By.XPATH, '//input[@placeholder={}]'.format(parameter))
        _lis = (By.XPATH, '//div[@class="el-select-dropdown el-popper"]'
                '//ul[@class="el-scrollbar__view el-select-dropdown__list"]'
                '/li/span[text()={}]'.format(val))
        self.find(self._robotKind).click()
        time.sleep(2)
        if len(self.finds(self._lis)) >1:
            self.finds(self._lis)[1].click()
        else:
            self.find(self._lis).click()

    def robot_kind(self, robot_kind):
        _robotKind = (By.XPATH, '//input[contains(@placeholder,"机器人类型")]')
        _lis = (By.XPATH, '//div[@class="el-select-dropdown el-popper"]//'
                          'ul[@class="el-scrollbar__view el-select-dropdown__list"]'
                          '/li/span[text()="{}"]'.format(robot_kind))
        print(_lis)
        self.finds(_robotKind)[-1].click()
        self.finds(_lis)[-1].click()

    def robots_kind(self, robots_kind):
        _robotGroupKind = (By.XPATH, '//input[contains(@placeholder,"机器人组类型")]')
        _lis = (By.XPATH, '//div[@class="el-select-dropdown el-popper"]//'
                          'ul[@class="el-scrollbar__view el-select-dropdown__list"]'
                          '/li/span[text()="{}"]'.format(robots_kind))
        self.finds(_robotGroupKind)[-1].click()
        self.finds(_lis)[-1].click()

    def to_home(self):
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        return self

    def scroll(self):
        _js = 'document.getElementsByClassName("el-table__body-wrapper is-scrolling-none")[0].scrollTop=10000'
        self.driver.execute_script(_js)
        time.sleep(3)


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
