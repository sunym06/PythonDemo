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

    def find(self, kv) -> WebElement:
        ele = self.driver.find_element(*kv)
        return ele
        # try:
        #     for i in range(3):
        #         ele = self.driver.find_element(by, value)
        #     return ele
        # except NoSuchElementException as e:
        #     print("找不到以下元素:")
        #     print(by, value)

    def finds(self, kv) -> list:
        time.sleep(2)
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
        # 点击下拉框后个别情况下点击不到元素，是因为点击后下拉框未及时加载出内容，
        # 而使用finds能够查到[-2]元素，故结束finds但未找到指定的元素

        _robotKind = (By.XPATH, '//input[contains(@placeholder,"机器人类型")]')
        # _lis = (By.XPATH, '//div[@class="el-select-dropdown el-popper"]//'
        #                   'ul[@class="el-scrollbar__view el-select-dropdown__list"]'
        #                   '/li/span[text()="{}"]'.format(robot_kind))
        li = (By.XPATH, '//li[contains(@class,"el-select-dropdown__item")]/span[text()="{}"]'.format(robot_kind))
        # print(_lis)
        self.finds(_robotKind)[-1].click()
        # time.sleep(2)
        print( '//li[contains(@class,"el-select-dropdown__item")]/span[text()="{}"]'.format(robot_kind))
        # self.finds(_lis)[-1].click()
        self.finds(li)[-1].click()

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

    def scroll(self, height):
        _js = 'document.getElementsByClassName("el-table__body-wrapper is-scrolling-none")[0].scrollTop={}'.format(height)
        self.driver.execute_script(_js)
        time.sleep(3)

    def list_option(self, name, option) ->WebElement:
        _name = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[text()="{}"]/../../../..//span[text()="{}"]'
                 .format(name, option))
        try:
            for i in range(3):
                ele = self.find(_name)
            ele.click()
        except:
            try:
                self.scroll(800)
                ele = self.find(_name).click()
            except:
                self.scroll(-800)
                ele = self.find(_name).click()
        return ele

    def cancel(self, cancel=False):
        _del = (By.XPATH, '//span[contains(text(),"确定")]')
        _cancel = (By.XPATH, '//span[contains(text(),"取消")]')
        if cancel:
            self.find(_cancel).click()
        else:
            self.find(_del).click()



if __name__ == "__main__":
    _url = 'http://www.baidu.com'
    _keyword = (By.ID, 'kw')
    pages = BasePage()
    driver = pages.driver
    driver.get(_url)
    pages.find(_keyword).send_keys('123')
    # driver.find(_keyword).send_keys('123')
    # print(dir(driver))
