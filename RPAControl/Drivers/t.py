# # # from selenium import webdriver
# # # import time
# # #
# # # web = webdriver.Chrome()
# # #
# # # web.get("http://www.jd.com")
# # # web.find_element_by_id('key').send_keys('背包')
# # # web.find_element_by_class_name('button').click()
# # # time.sleep(3)
# # # # 向下偏移了10000个像素，到达底部。
# # # js="var q=document.documentElement.scrollTop=10000"
# # # web.execute_script(js)
# # # time.sleep(5)
# # # #本来是只有30个元素，设置时间等待js动态加载，结果为60个元素。
# # # hah = web.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
# # # print(len(hah))
# # # web.close()
# #
# # from selenium import webdriver
# # import time
# #
# # web = webdriver.Chrome()
# #
# # web.get("http://www.jd.com")
# # web.find_element_by_id('key').send_keys('背包')
# # web.find_element_by_class_name('button').click()
# # time.sleep(3)
# #
# # js = 'document.getElementsByClassName("el-table__body-wrapper is-scrolling-none")[0].scrollTop=10000'
# # web.execute_script(js)
# # # target = web.find_element_by_id("service-2017")
# # # web.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
# # # time.sleep(15)
# # # hah = web.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
# # # print(len(hah))
# # # web.close()
# #
# # a = ("a", "B")
# # print(*a)
# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Ie()
# url = 'http://news.baidu.com/'
# driver.get(url)
# time.sleep(6)
#
#
# eles = driver.find_element_by_xpath('//span[text()="百家号"]')
# # ele = driver.find_element_by_xpath('//*[@id="footer"]/A[5]')
# ActionChains(driver).move_to_element(eles).perform()
# # print("page: " + driver.page_source)
# eles.click()
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('my_log')
logger.info('info message')
logger.debug('debug message')
logger.warning('warning message')


