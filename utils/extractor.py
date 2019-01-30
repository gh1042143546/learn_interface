import json
import jsonpath
from utils.client import Httpclient
class Extractor(object):
    def extract(self, body=None, query=None):
        try:
            return  jsonpath.jsonpath(json.loads(body),query)
        except Exception as e:
            raise ValueError("Invalid query: " + query + " : " + str(e))

if __name__ == '__main__':
    pass