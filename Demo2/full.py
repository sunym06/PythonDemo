from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://panjiachen.github.io/vue-element-admin/#/login?redirect=%2Fdashboard'
driver = webdriver.Chrome()
driver.get(url)
_user = (By.NAME, 'username')
_password = (By.NAME, 'password')
_loginbutton = (By.XPATH, '//span[contains(text()," 登录")]')
_table = (By.XPATH, '//span[text()="Table"]')
_table2 = (By.XPATH, '//span[text()="动态 Table"]')


# driver.find_element(*_user).send_keys('admin')
driver.find_element(*_password).send_keys('111111')
driver.find_element(*_loginbutton).click()
driver.find_element(*_table).click()
driver.find_element(*_table2).click()
