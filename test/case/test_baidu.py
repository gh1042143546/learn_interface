import pytest
import allure
from utils.assertion import assertHTTPCode
from utils.client import *
from utils.readCase import read_params
from utils.config import Config
'''
#@allure.feature("测试接口")
@pytest.fixture(params=['base_url'])
def readInfo(request):
    interfaceInfor = Config().get(request.param)#获取接口配置信息
    readyaml = read_params(r'../../date/cases/denglu.yaml')
    data = readyaml.get_params('data')
    #print(data)
    api_url = readyaml.get_params('Interface_Path')
    #print(api_url)
    method = readyaml.get_params('method')
    #print(method)
    return (api_url,method,data)
'''

def readInfo():
    denglu=[]
    readyaml = read_params(r'../../date/cases/denglu.yaml')
    url = readyaml.get_params('Interface_Path')
    method = readyaml.get_params('method')
    data = readyaml.get_params("data")
    denglu.append(url,method,data)


b = [['gatekeeper/api/auth/login','POST',{'verify_code': 2, 'password': 'testgroup', 'mobile': 13611849759},200], ['gatekeeper/api/auth/login','POST',{'verify_code': 2, 'password': 'testgroup', 'mobile': 13611849759},300]]



class TestBaiDuHTTP:
    #readyaml = read_params('/Users/lyg/PycharmProjects/learn_interface/date/cases/denglu.yaml')
    #data = readyaml.get_params('data')
    #b = readInfo()
    #print(b)
    '''
    @allure.story('测试登录接口')

    #@pytest.mark.parametrize(readInfo,readInfo)
    def test_tk(self,readInfo):
        c = Httpclient(readInfo[0][0],method=readInfo[1][0])
        #print(readInfo[2][0])
        response = c.sendRequest(param=readInfo[2][0])
        logger.info(response.text)
        assertHTTPCode(response, [200])
    '''
    @allure.story('测试登录接口')
    @pytest.mark.parametrize("url,method,date,hy",b)
    def test_case(self,url,method,date,hy):
        c = Httpclient(url,method=method)
        response = c.sendRequest(param=date)
        logger.info(response.text)
        assert response.status_code == hy
        #assertHTTPCode(response, [200])


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir','../report/'])