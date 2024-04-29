# import logging
import sys
import os
import pytest
from ddt import ddt,data,unpack
import jsonpath
from openxl import ReadExcel
from testpython.logs.logdata import Mylogger
from testpython.common.request1 import Sendsessionrequest
from datarequest import login_check





log1 = Mylogger()
log = log1.create_logging()

url1 = 'http://xh-test.zhidu30.xinhuimed.net/api/v3/login'
url2 = 'http://xh-test.zhidu30.xinhuimed.net/api/v3/ip_trust/lockUserUnbind?id=verificationLoginCode_admin_219&t=1714276610347'
header = {
    'Content-Type': 'application/json'
}


http = Sendsessionrequest()



@pytest.fixture(scope='class',autouse=True)

def my_fixture():
    pass

@ddt()
class TestDdt:

    excel = ReadExcel('test.xlsx', 'Sheet')
    cases = excel.read_data()
    # print(cases)

    @pytest.mark.parametrize('case1',cases)
    def test_login(self,case1):
        case_data = eval(case1['data'])
        expected = eval(case1['expected'])
        case_id = case1["case_id"]
        result_json = login_check(*case_data)
        response = http.send_requests(url=url1,json=result_json,method='post',header=header)
        http.send_requests(url=url2,method='get')
        result = response.json()

        try:
            assert expected['code'] == jsonpath.jsonpath(result,'$..code')[0]
            assert expected['msg'] == jsonpath.jsonpath(result,'$..msg')[0]
            # assert expected['msg' == result['msg']
        except AssertionError as e:
            log.info("用例：{}--->执行未通过".format(case1["title"]))
            print("预期结果：{}".format(expected))
            print("实际结果：{}".format(result))
            raise e
        else:
            log.info("用例：{}--->执行通过".format(case1["title"]))
            print("预期结果：{}".format(expected))
            print("实际结果：{}".format(result))

#
# if __name__ == '__main__':
#     # pytest.main(["r'--alluredir=data/allure'"])
#     # pytest.main(['-s', 'test_ddt2.py', '–alluredir', './ result'])

if __name__ == '__main__':
    pytest.main(['testddt2.py', '-s', '-q', '--alluredir', './result'])
    # os.system('allure generate ./result -o ./report --clean')