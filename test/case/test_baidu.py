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

class TestBaiDuHTTP:
    readyaml = read_params(r'../../date/cases/denglu.yaml')

    paramdate = readyaml.get_params()

    #@pytest.mark.parametrize("url,method,date,check",paramdate,ids=['正常登录','秘密错误'])
    #test_case_01为用例title
    #@allure.feature('登录模块')
    @allure.feature('登录模块')
    @allure.story('登录接口')
    @allure.issue("BUG号：123") # 问题表识，关联标识已有的问题，可为一个url链接地址
    @allure.testcase("用例名：登录校验")
    #@allure.Title("冒烟测试_所有算子运行_正常测试")
    @pytest.mark.parametrize("url,method,date,check",paramdate)
    # ids，对应用例参数化数据的用例名

    #@allure.description("测试一个流程，用作回归冒烟测试")
    def test_case(self,url,method,date,check):
        """用例描述：登录验证
        URL:参数一
        method:参数二
        date:参数三
        check:参数四
        """
        paras = vars()
        allure.attach("用例参数", "{0}".format(paras))
        c = Httpclient(url,method=method)
        response = c.sendRequest(param=date)
        logger.info(response.text)
        b = response.json()
        #assert b["code"] == check["code"]
            # 测试步骤，对必要的测试过程加以说明
        with pytest.allure.step("获取登录接口返回值，结果校验 {0} == {1}".format(b["code"], check["code"])):
            assert b["code"] == check["code"]


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir','../../result/'])