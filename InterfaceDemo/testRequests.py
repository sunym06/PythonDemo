import requests
import logging
import json


class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    url = 'https://testerhome.com/api/v3/topics.json?limit=2'
    proxies = {"http":"127.0.0.1:7788", "https":"127.0.0.1:7788"}
    json = {	"name":"tom",	"age":23,	"sex":"F" }
    def testGet(self):
        r = requests.get(self.url,params = {"name":"lily", "age":3}, verify = False, proxies= self.proxies)
        # logging.info(r)
        logging.info(json.dumps(r.json(), indent=2))
        # logging.info(r.url)
        logging.info(r.json()["topics"][0]["id"])
        # assert r.json()["topics"][0]["id"] == 21095

    def testCharles(self):
        r = requests.get('http://47.95.238.18:8090/get', proxies= self.proxies)
        logging.info(r.url)

    def testPost(self):
        # r = requests.post(self.url)
        # logging.info(r.headers)
        cok = dict( a = "test")
        r = requests.post(self.url, cookies= cok, proxies= self.proxies, verify = False)
        logging.info(r.cookies)

    def testPostHbin(self):
        cookies = dict(a = "a", b = "b")
        s = {"User-Agent": "python-requests/2.21.1"}
        url = 'http://47.95.238.18:8090/post'
        r = requests.post(url, proxies = self.proxies, cookies = cookies , json= self.json)
        # logging.info(r.url)
        # logging.info(r.cookies)
        # logging.info(r.json())
        logging.info(r.text)