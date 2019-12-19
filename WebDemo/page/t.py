# 调用JavaScript代码
# coding utf-8
from selenium import webdriver
from time import sleep

# 访问百度
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 设置浏览器窗口大下
# driver.set_window_size(500, 800)

# 搜索
driver.find_element_by_id('kw').send_keys('python selenium')
driver.find_element_by_id('su').click()
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100,850);"
driver.execute_script(js)  # 执行JavaScript代码
# driver.execute_async_script()
sleep(2)

driver.quit()