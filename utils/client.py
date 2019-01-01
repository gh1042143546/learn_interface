# -*- coding:utf-8 -*-
# Author:Gehao
import requests
import os
import time
from utils.config import Config,BASEURL_PATH



class Httpclient():
    def __init__(self,url):
       self.url = url
    #Config().get("local_url")

if __name__ == "__main__":
    c = Httpclient('yurl')
    print(c.url)