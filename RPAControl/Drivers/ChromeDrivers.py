from selenium import webdriver


class ChromeDrivers(object):

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    @classmethod
    def get_driver(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        return cls.driver


if __name__ == "__main__":
    a = ChromeDrivers.get_driver()

    # a.get('http://www.baidu.com')