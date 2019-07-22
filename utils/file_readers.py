# -*- coding:utf-8 -*-
import yaml
import os
import re
from  Utils import support
class YamlReader:
    def __init__(self,yamlfilePath):
        if os.path.exists(yamlfilePath):
            self.yamlfilePath = yamlfilePath
        else:
            raise FileNotFoundError('文件不存在！')
    def read_date(self):
        file = open(self.yamlfilePath,encoding='UTF-8')
        date = list((yaml.load_all(file)))
        return date
    def read_case(self):
        file = open(self.yamlfilePath,encoding='UTF-8')
        casedate = yaml.load(file)
        return casedate
if __name__== '__main__':
    testdata = []
    reader = YamlReader('../date/cases/denglu.yaml')
    res = reader.read_case()
    case_string = res[0]["variable_binds"]
    regex = r"^\$\{(\w+)\((.*)\)\}$"
    for i in case_string:
        for key,values in i.items():
            print(key,values)
            matched = re.match(regex, values)
            func = matched.group(1)
            arg = matched.group(2)
            obj = getattr(support, func)
            i[key] =obj(arg)
            print(i)
    #b = str(case_string)
    '''
    regex = r"^\$\{(\w+)\((.*)\)\}$"
    matched = re.match(regex, case_string)
    func = matched.group(1)
    arg = matched.group(2)
    print(func,arg)
    '''