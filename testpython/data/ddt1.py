from ddt import ddt, data

from common.read_excel import ReadExcel
from common.my_logger import log


@ddt  # 装饰登录测试用例类，声明使用ddt
class LoginTestCase(unittest.TestCase):
    excel = ReadExcel("cases.xlsx", "login")
    cases = excel.read_data()

    @data(*cases)  # 装饰测试用例
    def test_login(self, case):
        case_data = eval(case["data"])
        expected = eval(case["expected"])
        case_id = case["case_id"]
        result = login_check(*case_data)
        response = self.http.send(url=url, method=method, json=data, headers=headers)
        result = response.json()
        try:
            self.assertEqual(expected["code"], result["code"])
            self.assertEqual((expected["msg"]), result["msg"])
        except AssertionError as e:
            log.info("用例：{}--->执行未通过".format(case["title"]))
            print("预期结果：{}".format(expected))
            print("实际结果：{}".format(result))
            raise e
        else:
            log.info("用例：{}--->执行通过".format(case["title"]))


if __name__ == '__main__':
    unittest.main()