import pytest

from testpython.drivers import testdriver


from testpython.testdata.openxl import ReadExcel

from testpython.logs.logdata import Mylogger
#
#
# dir = testdriver.Login(url1='http://xh-test.zhidu30.xinhuimed.net/v3/#/login')
text1 = '现代化医院制度数字化应用平台'

my_logs = Mylogger()
my_log = my_logs.create_logging()

# xh = ReadExcel(file_name='test1.xlsx',sheet_name='sheet1')
try:
    xh = ReadExcel(file_name='test1.xlsx', sheet_name='sheet1')
    # xh.save()
    xh.write_data(row=1, colunn=1, msg='账号')
    xh.write_data(row=1, colunn=2, msg='密码')
    xh.write_data(row=1, colunn=3, msg='信息')
    xh.write_data(row=2, colunn=1, msg='admin')
    xh.write_data(row=2, colunn=2, msg='Xh@2022!@#')
    xh.write_data(row=2, colunn=3, msg='现代化医院制度数字化应用平台')
    data = xh.read_data()
    # print(data)
except Exception as msg:
    my_log.error('数值输入不正确')
    # print(data)

else:
    my_log.info('可以输出')




@pytest.fixture(scope='class',autouse=True)



def my_fixture():
    dir = testdriver.Login(url1='http://xh-test.zhidu30.xinhuimed.net/v3/#/login')
    yield dir
    print('前置条件')

# 模板名 test_*.py
# 类名 Test开头
# 方法名 test_

class TestLogin:


    def test_login1(self,my_fixture):
        dir = my_fixture
        text2  =dir.login()
        print('第一次尝试登录')
        assert text1 == text2
    #
    # def test_login2(self,my_fixture):
    #     dir = my_fixture
    #     text2  = dir.login()
    #     print('第二次尝试登录')
    #     assert text1 == text2

    # def test_login2():
    #     text2  = dri.login(username='852369',password='Aa123456*',captcha_code='6666')
    #     assert text1 == text2
    # def test_login3():
    #     text2  = dri.login(username='8523691',password='Aa123456*',captcha_code='6666')
    #     assert text1 == text2
    # # def test_login3():


if __name__ == '__main__':
    pytest.main()



