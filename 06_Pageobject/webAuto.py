import time

from selenium import webdriver

url = 'http://192.168.9.35:1888/#/login'
url1 = 'http://192.168.9.36:1888/#/login'

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(20)

user_xpath = '//div[@class="el-form-item__content"]//input[@type="text"]'
pwd_xpath = '//div[@class="el-form-item__content"]//input[@type="password"]'
but_xpath = '//div[@class="el-form-item__content"]/button'

driver.find_element_by_xpath(user_xpath).clear()
driver.find_element_by_xpath(   user_xpath).send_keys('admin')
driver.find_element_by_xpath(pwd_xpath).clear()
driver.find_element_by_xpath(pwd_xpath).send_keys('111111')
driver.find_element_by_xpath(but_xpath).click()

# menu1_xpath = '//span[text()="工作流管理"]'
# menu2_xpath = '//span[text()="调度计划管理"]'
# menu22_xpath = '//span[text()="参数管理"]'
T1_flow = '//span[text()="流程模板管理"]/..'
T2_mod = '//span[text()="流程模板"]/..'
ct_imp = '//span[text()="导入"]/..'
int = '//input[@placeholder="请选择流程类型"]/../span'
li_cl = '//div[@class="el-dialog__body"]//label[text()="流程类型"]/..//span[@class="el-input__suffix"]'
li1 = '//li[@class="el-select-dropdown__item selected hover"]'
li2 = '.el-select-dropdown__item.hover'
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath(T1_flow).click()
time.sleep(3)
driver.find_element_by_xpath(T2_mod).click()
time.sleep(3)
driver.find_element_by_xpath(ct_imp).click()
time.sleep(2)
driver.find_element_by_xpath(int).click()
time.sleep(2)
# driver.find_element_by_xpath(li1).click()
driver.find_element_by_css_selector(li2).click()