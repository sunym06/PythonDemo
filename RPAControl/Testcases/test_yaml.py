import yaml


class Test_yaml():

    def test_yaml(self):
        # A = {"a": "123"}
        strings = yaml.load(open('../data/login.yaml', 'r'))
        print(strings)
        print(strings["loginPage"][0]["name"])
        for i in strings['loginPage'][0]:
            print()