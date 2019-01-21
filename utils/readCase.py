import yaml
from utils.file_reader import YamlReader
class read_params:
    def __init__(self,path):
        self.reader  = YamlReader(path)
        #print(reader.read_case())
    def get_params(self):
        params = self.reader.read_case()
        for i in params:
            print(i)
            #print(i['denglu'][0]['method'])
        print(params)
if __name__== '__main__':
    b = read_params('../date/cases')
    b.get_params()