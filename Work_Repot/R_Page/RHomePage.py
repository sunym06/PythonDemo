from selenium.webdriver.common.by import By

from Work_Repot.R_Page.RBasePage import RBasePage
from Work_Repot.R_Page.RReportPage import RReportPage


class RHomePage(RBasePage):

    def sheet(self, st):
        _location = (By.XPATH, '//a[@title="{}"]'.format(st))
        self.find(_location).click()

    def to_work(self):
        self.sheet("报工系统")
        return RReportPage()

    def report_list(self):
        self.find