import pytest
import os
from utils.log import logger

if __name__ == '__main__':
    path_dir = os.path.split(os.path.realpath(__file__))[0]#项目目录
    Testresult_path = path_dir+"/result"
    print(Testresult_path)

    Testreport_path = path_dir+"/report"
    allure_list="--allure_features=登录模块"
    b  = os.getcwd()
    print("当前工作目录"+b)
    args = ['-s', '-q', '--alluredir', Testresult_path]
    #pytest.main(args)
    pytest.main(args)
    a  = os.getcwd()
    print("当前工作目录"+a)
    cmd = 'allure generate %s -o %s --clean' % (Testresult_path, Testreport_path)

    try:
        os.system(cmd)
    except Exception:
        logger.error('执行用例失败，请检查环境配置')
        raise
tester