# -*- coding:utf-8 -*-
import yaml
from utils.file_reader import YamlReader
class read_params:
    def __init__(self,path):
        self.reader  = YamlReader(path)

    def get_params(self,param):
        params = self.reader.read_case()
        print(params)
        paramdate = []
        for i in params:
            paramdate.append(i[param])
        return paramdate
if __name__== '__main__':
    b = read_params('../date/cases/denglu.yaml')
    print(b.get_params('data'))
