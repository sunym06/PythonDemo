from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Drivers(object):

    driver: WebDriver

    def __init__(self):
        self.driver = webdriver.Chrome()

