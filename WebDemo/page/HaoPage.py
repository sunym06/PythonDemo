from selenium.webdriver.common.by import By
from WebDemo.page.BasePage import BasePage
# from WebDemo.page.MainPage import MainPage


class HaoPage(BasePage):
    _pepole = (By.XPATH, '//a[text()="人民网"]')

    # def __init__(self):
        # pass

    def to_people(self):
        # Drivers = ChromeDrivers.get_driver()
        # self.Drivers.find_element((By.XPATH, '//a[text()="人民网"]')).click()
        # .get_driver().find_element((By.XPATH, '//a[text()="人民网"]')).click()
        # self.Drivers.find_element(By.XPATH, '//a[text()="人民网"]').click()
        self.drivers.find(By.XPATH, '//a[text()="人民网"]').click()
        # self.Drivers.find_element(By.XPATH, '//a[text()="人民网"]').click()
        # ChromeDrivers.get_driver().find_element(By.XPATH, '//a[text()="人民网"]').click()


# if __name__ == "__main__":
#     a = MainPage().to_hao123().to_people()
#     # a.to_people()
