# # from RPAControl.ds import T
# # from RPAControl.sdf import Ts
# #
# #
# # class M (T, Ts):
# #     M=123
# #     def PP(self):
# #         print(self.M)
# #         self.p()
# #         self.p2()
# #
# # a = M()
# # a.PP()
# # #
# # import random
# # l = [1,2,4,5,6,7,75,4645,645,23]
# #
# # for i in range(12):
# #     # s = random.choice(l)
# #     # ss = random.sample(l,1)
# #     # print(ss)
# #     sel = random.sample([0, 1], 1)
# #     print(sel)
#
# # from selenium import webdriver
# # driver = webdriver.Chrome()
# # driver.get('http://localhost:10000/iframe.html')
# # driver.switch_to.frame('four')
# # driver.find_element_by_id('username').send_keys('123')
# import xlrd
# file = 'C:/sunym/03_workspace/00_PythonWorkspac/RPAControl/data.xlsx'
# # with open(file, 'r') as f:
# data = xlrd.open_workbook(file)
# table = data.sheet_by_index(0)
# keys = table.row_values(0)
# rows = table.nrows
# clo = table.ncols
# print(keys, rows, clo)
# s = []
# for i in range(1, rows - 1):
#     r = tuple(table.row_values(i))
#     s.append(r)
#
# print(s)
# for i in range(1, 5):
#     print(i)
#
a = [1,2,4,6]
b = [3]
c = a.append(b)
print(a)