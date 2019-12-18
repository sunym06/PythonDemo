class tes():

    def add(self, a, b):
        return a+b

    def t(self, s):
        return tes().add(3, 5) + s


if __name__ == "__main__":
    a = tes()
    t = a.t(2)
    print(t)