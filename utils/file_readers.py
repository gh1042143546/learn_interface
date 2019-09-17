# -*- coding:utf-8 -*-
import yaml
import os
import re
from utils import support
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
    path_dir = os.path.split(os.path.realpath(__file__))[0]#项目目录
    reader = YamlReader('../date/cases/denglu.yaml')
    reader.read_case()