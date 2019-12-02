from selenium.webdriver.chrome.webdriver import WebDriver
from WebDemo.drivers.ChromeDriver import ChromeDriver
# from WebDemo.pages.FirstPage import FirstPage


class LoginPage(object):
    driver: WebDriver = ChromeDriver.get_driver()

    # @classmethod
    def login(self, user:str, pwd:str):
        user_xpath = '//div[@class="el-form-item__content"]//input[@type="text"]'
        pwd_xpath = '//div[@class="el-form-item__content"]//input[@type="password"]'
        but_xpath = '//div[@class="el-form-item__content"]/button'

        self.driver.find_element_by_xpath(user_xpath).clear()
        self.driver.find_element_by_xpath(user_xpath).send_keys(user)
        self.driver.find_element_by_xpath(pwd_xpath).clear()
        self.driver.find_element_by_xpath(pwd_xpath).send_keys(pwd)
        self.driver.find_element_by_xpath(but_xpath).click()
        # return FirstPage


