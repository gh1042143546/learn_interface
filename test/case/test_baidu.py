import pytest
import allure
from utils.assertion import assertHTTPCode
from utils.client import *
from utils.readCase import read_params
from utils.config import Config

#@allure.feature("测试接口")
@pytest.fixture(params=['denglu'])
def readInfo(request):
    interfaceInfor = Config().get(request.param)#获取接口配置信息
    readyaml = read_params('/Users/lyg/PycharmProjects/learn_interface/date/cases/denglu.yaml')
    data = readyaml.get_params('data')
    api_url = interfaceInfor['api']
    method = interfaceInfor['method']
    return (api_url,method,data)


class TestBaiDuHTTP:
    #readyaml = read_params('/Users/lyg/PycharmProjects/learn_interface/date/cases/denglu.yaml')
    #data = readyaml.get_params('data')
    #@allure.story('测试登录接口')
    def test_tk(self,readInfo):
        c = Httpclient(readInfo[0],readInfo[1])
        response = c.sendRequest(readInfo[2])
        logger.info(response.text)
        assertHTTPCode(response, [200])

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir','../../report/'])