from selenium.webdriver.chrome.webdriver import WebDriver
from RPA.drivers.ChromeDriver import ChromeDriver

# from WebDemo.pages.FirstPage import FirstPage


class DemoPage(object):
    driver: WebDriver = ChromeDriver.get_driver()
    _user_xpath = '//div[@class="el-form-item__content"]//input[@type="text"]'
    _pwd_xpath = '//div[@class="el-form-item__content"]//input[@type="password"]'
    _but_xpath = '//div[@class="el-form-item__content"]/button'

    def login(self, user: str, pwd: str):

        self.driver.find_element_by_xpath(self._user_xpath).clear()
        self.driver.find_element_by_xpath(self._user_xpath).send_keys(user)
        self.driver.find_element_by_xpath(self._pwd_xpath).clear()
        self.driver.find_element_by_xpath(self._pwd_xpath).send_keys(pwd)
        self.driver.find_element_by_xpath(self._but_xpath).click()
        # return FirstPage


