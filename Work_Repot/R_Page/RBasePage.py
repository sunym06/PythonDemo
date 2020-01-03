from Work_Repot.GetDriver.GetDriver import GetDriver


class RBasePage(object):

    driver = GetDriver().driver

    def find(self, kv):
        return self.driver.find_element(*kv)

    # def type_into(self, value):


if __name__ == "__main__":
    a = RBasePage.driver.get('http://www.baidu.com')