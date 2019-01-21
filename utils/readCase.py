import yaml
from utils.file_reader import YamlReader
class read_params:
    def __init__(self,path):
        self.reader  = YamlReader(path)
        #print(reader.read_case())
    def get_params(self):
        params = self.reader.read_case()
        print(params)
if __name__== '__main__':
    b = read_params('/Users/lyg/PycharmProjects/learn_interface/date/cases')
    b.get_params()