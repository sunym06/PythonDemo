import time

from selenium.webdriver.chrome.webdriver import WebDriver

from WebDemo.drivers.ChromeDriver import ChromeDriver


class FirstPage(object):

    driver: WebDriver = ChromeDriver.get_driver()
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
    # todo 定位不到下拉框内容，无法点击
    driver.find_element_by_css_selector(li2).click()