# import time
# import pytest
# from selenium import webdriver
#
#
#
# #
# #
# # class Tem(object):
# #     _url = 'http://www.baidu.com'
# #
# #     # def __init__(self):
# #     #     self.driver = webdriver.Chrome()
# #     #     self.driver.get(self._url)
# #
# #     @classmethod
# #     def get(cls):
# #         cls.driver = webdriver.Chrome()
# #         cls.driver.get(cls._url)
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# driver.find_element_by_xpath('//a[text()="新闻"]').click()
# time.sleep(10)
# # driver.find_element_by_xpath('//li[@class="hdline0"]').click()
# driver.find_element_by_xpath('//li[@class="hdline0"]').click()
# # hands = driver.window_handles
# # print(hands)
# # for i in hands:
# #     driver.find_element_by_xpath('//a[text()="打开"]').click()
#

class Student():
    age: int
    score: int
    name = 'tom'
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
    def __str__(self):
        return 'self '
a = Student()
b = Student()
# print(a.age)
print(a.name)
# print(a)
a

    # @property
    # def birth(self):
    #         return self._birth
    #
    # @birth.setter
    # def birth(self, value):
    #     self._birth = value
    #
    # @property
    # def age(self):
    #     return 2015 - self._birth
#
# a = Student()
# # print(a.score)
# a.score = 25
# print(a.score)
