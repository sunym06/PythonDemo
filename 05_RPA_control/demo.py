import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

_user = (By.NAME, 'username')
_password = (By.NAME, 'password')
_login = (By.XPATH, '//span[text()="登录"]')
url = 'http://192.168.8.222:8111/#/login'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.find_element(*_user).clear()
driver.find_element(*_user).send_keys('admin')
driver.find_element(*_password).clear()
driver.find_element(*_password).send_keys('111111')
driver.find_element(*_login).click()


_robotM = (By.XPATH, '//span[text()="机器人管理"]')
_robot = (By.XPATH, '//span[text()="机器人"]')
_add = (By.XPATH, '//span[text()="新 增"]')
time.sleep(3)
driver.find_element(*_robotM).click()
time.sleep(2)
driver.find_element(*_robot).click()
time.sleep(2)
# driver.find_element(*_add).click()

_rotName = (By.XPATH, '//input[@placeholder="请输入 机器人名称"]')
_rotkind = (By.XPATH, '//input[@placeholder = "请选择 机器人类型"]')
_description = (By.XPATH, '//textarea[@placeholder = "请输入 描述"]')

# _li = (By.XPATH, '//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[@class="el-select-dropdown__item hover"]/..')
_li = (By.XPATH, '//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[text()="无人值守"]')
_save = (By.XPATH, '//span[text()="保 存"]')
_li3 = (By.XPATH, '//ul[@class="el-scrollbar__view el-select-dropdown__list"]//span[text()="无人值守"]')
# driver.find_element(*_rotName).send_keys('the new one')
# driver.find_element(*_rotkind).click()
# time.sleep(3)
# li = driver.find_element(*_li)
# Select(li).select_by_index(0)
# select = Select(driver.find_element(*_li))
# select.select_by_index(0)
# driver.find_elements(*_li)[1].click()
# driver.find_element(*_description).send_keys("add description ")
# driver.find_element(*_save).click()

_li2 = (By.XPATH, '//input[@placeholder="机器人类型"]/..')
_search = (By.XPATH, '//span[text()="搜 索"]')
driver.find_element(*_li2).click()
time.sleep(5)
driver.find_element(*_li3).click()
driver.find_element(*_search).click()
_message = (By.XPATH, '//p[@class="el-message__content"]')



