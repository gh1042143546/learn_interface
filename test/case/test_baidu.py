import pytest
import allure
from utils.assertion import assertHTTPCode
from utils.client import *
#@allure.feature("测试接口")
class TestBaiDuHTTP():
    #@allure.story('测试登录接口')
    def test_tk(self):
        c = Httpclient('/login.jhtml','GET')
        response = c.sendRequest({"userAccount":"admin","password":"Pass123456"})
        logger.info(response.text)
        assertHTTPCode(response, [200])

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir','../../report/'])
