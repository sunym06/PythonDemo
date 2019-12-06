from WebDemo.demo.BaiduPage import BaiduPage
import pytest


class Test_easy():
    def test_click(self):
        BaiduPage().to_news().to_tie()


if __name__ == "__main__":
    pass
