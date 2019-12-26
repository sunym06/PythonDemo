from RPAControl.ds import T
from RPAControl.sdf import Ts


class M (T, Ts):
    M=123
    def PP(self):
        print(self.M)
        self.p()
        self.p2()

a = M()
a.PP()

