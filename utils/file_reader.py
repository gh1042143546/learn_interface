# -*- coding:utf-8 -*-
import yaml
import os
class YamlReader:
    def __init__(self,yamlfilePath):
        if os.path.exists(yamlfilePath):
            self.yamlfilePath = yamlfilePath
        else:
            raise FileNotFoundError('文件不存在！')
    def read_date(self):
        file = open(self.yamlfilePath)
        date = list((yaml.load_all(file)))
        return date
    def read_case(self):
        files = os.listdir(self.yamlfilePath)
        date = []
        for i in files:
            file = open(os.path.join(self.yamlfilePath,i))
            b = yaml.load(file)
            date.append(b)
        return date
        #print(os.path.join())
if __name__== '__main__':
    reader = YamlReader('../date/cases')
    print(reader.read_case())
    #print(reader.read_date())