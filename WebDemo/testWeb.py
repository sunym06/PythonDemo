from selenium import webdriver
import logging
import pytest


class TestWeb(object):
    url = 'www.baidu.com'

    def testDriver(self):
        driver = webdriver.Chrome()
        driver.get(self.url)