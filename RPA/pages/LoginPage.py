from selenium.webdriver.chrome.webdriver import WebDriver
from RPA.drivers.ChromeDriver import ChromeDriver

# from WebDemo.pages.FirstPage import FirstPage


class LoginPage(object):
    driver: WebDriver = ChromeDriver.get_driver()

    @classmethod
    def login(cls, user: str, pwd: str):
        user_xpath = '//div[@class="el-form-item__content"]//input[@type="text"]'
        pwd_xpath = '//div[@class="el-form-item__content"]//input[@type="password"]'
        but_xpath = '//div[@class="el-form-item__content"]/button'

        cls.driver.find_element_by_xpath(user_xpath).clear()
        cls.driver.find_element_by_xpath(user_xpath).send_keys(user)
        cls.driver.find_element_by_xpath(pwd_xpath).clear()
        cls.driver.find_element_by_xpath(pwd_xpath).send_keys(pwd)
        cls.driver.find_element_by_xpath(but_xpath).click()
        # return FirstPage


