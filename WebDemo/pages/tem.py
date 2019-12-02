# 调用login，当引用的LoginPage将login写为类方法时可直接 class.method，如login为普通方法则需要 class().method
# from WebDemo.pages.LoginPage import LoginPage
# LoginPage.login('admin', '111111')
from WebDemo.pages.LoginPage import LoginPage

LoginPage().login('admin', '111111')

