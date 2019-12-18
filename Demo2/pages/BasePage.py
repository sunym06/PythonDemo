from Demo2.drivers.Drivers import Drivers


class BasePage(object):

    def __init__(self):
        self.driver = Drivers().driver


if __name__ == "__main__":
    a = BasePage()