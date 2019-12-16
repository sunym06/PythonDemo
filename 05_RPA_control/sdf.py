from selenium import webdriver

url = 'http://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)

li = driver.find_elements_by_xpath('//a[@class="mnav"]')
print(type(li))
li[5].click()
