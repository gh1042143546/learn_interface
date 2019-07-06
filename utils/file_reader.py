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
        file = open(self.yamlfilePath,encoding='UTF-8')
        date = list((yaml.load_all(file)))
        return date
    def read_case(self):
        file = open(self.yamlfilePath,encoding='UTF-8')
        casedate = yaml.load(file)#返回一个字典

        return casedate
if __name__== '__main__':
    reader = YamlReader('../date/cases/denglu.yaml')
    print(reader.read_case())