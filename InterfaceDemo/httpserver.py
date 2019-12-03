from selenium import webdriver
import time

url = 'https://www.baidu.com'

driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_id('kw').send_keys('李世雄')
driver.find_element_by_id('su').click()
time.sleep(3)
driver.find_element_by_xpath('//div[@class="s_tab_inner"]/a[contains(text(),"图片")]').click()