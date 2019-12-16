import time

from selenium import webdriver

driver = webdriver.Chrome()
url = 'http://192.168.8.222:8111/#/login'
driver.get(url)
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('111111')
driver.find_element_by_css_selector('.el-button.el-button--primary.el-button--small').click()

time.sleep(30)

driver.find_element_by_xpath('//span[text()="流程模板管理"]').click()
time.sleep(10)
driver.find_element_by_xpath('//li//span[text()="流程模板"]').click()
time.sleep(10)
driver.find_element_by_xpath('//span[text()="导入"]').click()

