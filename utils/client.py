# -*- coding:utf-8 -*-
# Author:test
import requests
import os
import time
from utils.config import Config,BASEURL_PATH
from utils.log import logger
METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']  # 所有支持的前后前交互方法

class Httpclient():
    def __init__(self,url,method='GET',headers=None,cookies=None):
        #self.url = url
        global base_url
        congFig = Config()
        base_url = congFig.get("base_url")
        self.url = base_url+url
        self.params = {}
        self.method = method
        self.session = requests.session()#返回一个session类
        if self.method not in METHODS:
            raise Exception('不支持的method:{0}，请检查传入参数！'.format(self.method))
        #print(base_url)
    def set_header(self,headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def set_url(self,url):
        self.url = base_url + url

    def set_param(self,params):
        self.params=params

    def sendRequest(self,param=None,data=None):
        response = self.session.request(method=self.method,url=self.url,params=param,data=data)
        logger.info('{0} {1}'.format(self.method, self.url))
        logger.info(('请求成功: {0}\n{1}'.format(response, response.text)))
        return response

if __name__ == "__main__":
    pass