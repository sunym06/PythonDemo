from Demo2.drivers.Drivers import Drivers
from Demo2.pages.BasePage import BasePage
from Demo2.pages.LoginPage import LoginPage


class MainPage(BasePage):
    url = 'https://panjiachen.github.io/vue-element-admin/#/login?redirect=%2Fdashboard'

    def main(self):
        Drivers().driver.get(self.url)
        return LoginPage()


