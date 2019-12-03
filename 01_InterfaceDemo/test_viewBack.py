import requests
import pytest
import logging


class TestRequests(object):
    url = 'https://www.baidu.com'
    logging.basicConfig(level= logging.INFO)
    def testGet(self):
        r = requests.get(self.url)
        logging.info(r.text)

    def testEA(self):
        pass

    def testssd(self):
        pass