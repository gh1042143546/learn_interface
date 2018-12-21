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
if __name__== '__main__':
    reader = YamlReader('/Users/lyg/PycharmProjects/learn_interface/config/config.yml')
    print(reader.read_date())