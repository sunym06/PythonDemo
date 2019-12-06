import time

from selenium import webdriver
#
#
# class Tem(object):
#     _url = 'http://www.baidu.com'
#
#     # def __init__(self):
#     #     self.driver = webdriver.Chrome()
#     #     self.driver.get(self._url)
#
#     @classmethod
#     def get(cls):
#         cls.driver = webdriver.Chrome()
#         cls.driver.get(cls._url)

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_xpath('//a[text()="新闻"]').click()
time.sleep(10)
# driver.find_element_by_xpath('//li[@class="hdline0"]').click()
driver.find_element_by_xpath('//li[@class="hdline0"]').click()
# hands = driver.window_handles
# print(hands)
# for i in hands:
#     driver.find_element_by_xpath('//a[text()="打开"]').click()