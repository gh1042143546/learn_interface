# -*- coding:utf-8 -*-
import pytest
import allure
#from utils.assertion import assertHTTPCode
from Utils.client import *
from Utils.readCase import read_params
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
    path_dir = os.path.split(os.path.realpath(__file__))[1]#项目目录
    print(path_dir)
    readyaml = read_params(r'/learn_interface/date/cases/denglu.yaml')
    paramdate = readyaml.get_params()
    #print(paramdate)S
    #paramdate=[('gatekeeper/api/auth/login', 'POST', {'verify_code': 2, 'password': 123456, 'mobile': 18016220960}, {'code': 0, 'message': 'success'}), ('gatekeeper/api/auth/login', 'POST', {'verify_code': 2, 'password': None, 'mobile': 18016220960}, {'code': 1, 'message': '密码不能为空。'})]
    @allure.feature('登录模块')
    @allure.story('登录接口')
    @allure.issue("BUG号：123") # 问题表识，关联标识已有的问题，可为一个url链接地址
    @allure.testcase("用例名：登录校验")
    @allure.title("冒烟测试_所有算子运行_正常测试")
    @pytest.mark.parametrize("url,method,date,check",paramdate,ids=["正常登录","异常登录"])# ids，对应用例参数化数据的用例名
    def test_case(self,url,method,date,check):
        """用例描述：登录验证
        URL:参数一
        method:参数二
        date:参数三
        check:参数四
        """
        paras = vars()
        allure.attach("用例参数", "{0}".format(paras))
        c = Httpclient(url=url,method=method)
        response = c.sendRequest(param=date)
        logger.info(response.text)
        b = response.json()
        # 测试步骤，对必要的测试过程加以说明
        with allure.step("获取登录接口返回值，结果校验 {0} == {1}".format(b["code"], check["code"])):
            assert b["code"] == check["code"],"判断返回码，当前code的值为：%s"%b["code"]
            assert b["message"] == check["message"]


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir','../../result/'])
