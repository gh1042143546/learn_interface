# -*- coding: utf-8 -*-
import json
import jsonpath
from utils.client import Httpclient
class Extractor(object):
    def __init__(self,body):
        if  isinstance(body,dict):
            self.body=body

    def extract(self,query=None):
        try:
            return  jsonpath.jsonpath(self.body,query)
        except Exception as e:
            raise ValueError("Invalid query: " + query + " : " + str(e))


if __name__ == '__main__':
    d={
        "error_code": 0,
        "stu_info": [
                {
                        "id": 2059,
                        "name": "小白",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "18378309272",
                        "gold": 10896,
                        "info":{
                            "card":434345432,
                            "bank_name":'中国银行'
                        }

                },
                {
                        "id": 2067,
                        "name": "小黑",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "12345678915",
                        "gold": 100
                }
        ]
}
    b = Extractor(d)
    w = b.extract('$.error_code')
    print(w)