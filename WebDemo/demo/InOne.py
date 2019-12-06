from selenium import webdriver

url = 'http://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath('//a[text()="新闻"]').click()
driver.find_element_by_xpath('//a[text()="贴吧"]').click()