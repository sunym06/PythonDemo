import requests
import logging
import json


class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    def testGet(self):
        r = requests.get('https://testerhome.com/api/v3/topics.json?limit=2')
        logging.info(r)
        logging.info(json.dumps(r.json(), indent=4))
