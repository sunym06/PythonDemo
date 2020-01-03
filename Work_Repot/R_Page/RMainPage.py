from Work_Repot.R_Page.RBasePage import RBasePage
from Work_Repot.R_Page.RLoginPage import RLoginPage


class RMainPage(RBasePage):
    _url = 'http://124.193.68.238:8081/cas/' \
           'login?service=http%3A%2F%2F124.193.68.238%3A8085%2Fx5mini%2Fj_spring_cas_security_check'

    def start(self):
        self.driver.get(self._url)
        return RLoginPage()


if __name__ == "__main__":
    a = RMainPage().start()
