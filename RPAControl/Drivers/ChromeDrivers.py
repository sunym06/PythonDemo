from selenium import webdriver


class ChromeDrivers(object):

    @classmethod
    def get_driver(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        return cls.driver


if __name__ == "__main__":
    driver = ChromeDrivers.get_driver()
    driver.get('http://www.baidu.com')

