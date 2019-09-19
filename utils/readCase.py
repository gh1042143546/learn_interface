# -*- coding:utf-8 -*-
from utils.file_readers import YamlReader

class read_params:
    def __init__(self,path):
        self.reader = YamlReader(path)
    '''
    def get_params(self,param):
        params = self.reader.read_case()
        paramdate = []
        for i in params:
            paramdate.append(i[param])
        return paramdate
    '''
    def get_params(self):
        '''
        :return:返回接口请求需要的参数
        '''
        paramdate = []
        Testdata = self.reader.read_case()
        for param in Testdata:
            url = param["Interface_Path"]
            method = param["method"]
            data = param["data"]
            check = param["check"]
            t=(url,method,data,check)
            paramdate.append(t)
        return paramdate

if __name__== '__main__':
    b = read_params('../date/cases/denglu.yaml')
    print(b.get_params())
qwer