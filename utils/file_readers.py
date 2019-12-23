# -*- coding:utf-8 -*-
from gooey import Gooey,GooeyParser
import yaml
import os
import re
from utils import support

class YamlReader:
    parser = GooeyParser(description="My Cool Gooey App!")
    parser.add_argument('yamlfilePath', help="name of the file to process", widget='FileChooser')
    def __init__(self,yamlfilePath):
        if os.path.exists(yamlfilePath):
            self.yamlfilePath = yamlfilePath
        else:
            raise FileNotFoundError('文件不存在！')

    def read_date(self):
        file = open(self.yamlfilePath,encoding='UTF-8')
        date = list((yaml.load_all(file,Loader=yaml.FullLoader)))
        return date

    def read_case(self):
        file = open(self.yamlfilePath,encoding='UTF-8')
        casedate = yaml.load(file,Loader=yaml.FullLoader)
        return casedate
#这里没有
if __name__== '__main__':
    path_dir = os.path.split(os.path.realpath(__file__))[0]#项目目录
    reader = YamlReader('../date/cases/denglu.yaml')
    b = reader.read_case()
    print(b)#输出