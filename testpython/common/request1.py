import requests
import json
import jsonpath

class Sendsessionrequest:

    def __init__(self):
        self.session = requests.session()

    def send_requests(self, url, method, data=None, json=None, param=None, header=None):
        self.method = method
        try:
            if self.method == 'get':
                return self.session.get(url=url, params=param)
            elif self.method == 'post':
                return self.session.post(url=url, data=data, json=json, headers=header)
            elif self.method == 'put':
                pass
            else:
                print('没有值')
                return None

        #
        except Exception as e:
            print('错误')
            return f'发生了错误:{e}'



if __name__ == '__main__':
    xh = Sendsessionrequest()
    url1 = 'http://xh-test.zhidu30.xinhuimed.net/api/v3/login'
    header = {
        'Content-Type': 'application/json'

    }

    json1 = {
        'username': 'J/fY3PE2HH0kvMZzbv5BLQ==',
        'password': 'ez27Us6DpzGoPNkb3FH/Mw==',
        'captcha': '',
        'captcha_code': '6666',
        'captcha_key': '$2y$10$reArgS92v9zKSj.Z77yls.nqw0mxi1gVyEVzu.eYv9vT6/2DS8Z9q',
        'type': 'username',
        'mobile': '',
        'sms_code': ''}
    gh = xh.send_requests(url=url1, header=header,method='post',json=json1 )
    # print(gh.json())
    # print(gh.text)
    gh1 = gh.json()
    ghh = json.loads(gh.text)
    ghh1 = json.dumps(gh.text,sort_keys=True, indent=4, separators=(',', ': '))
    print(ghh)
    msg = jsonpath.jsonpath(gh1,'$..msg')[0]
    token1 = jsonpath.jsonpath(gh1,'$..token')[0]

    print('msg是{}'.format(msg))
    print('token1是{}'.format(token1))









    url2 ='http://xh-test.zhidu30.xinhuimed.net/api/v3/setting/config'

    sh = xh.send_requests(url=url2, param=None, method='get')





















    # gh1 = json.loads(sh.text)
    # # data = sh.text
    # # print(json.loads(data, sort_keys=True, indent=4, separators=(',', ': ')))
    #
    # print(gh1)
    # # print(sh.text)





#
# se = requests.session()
#
# url1 = 'http://xh-test.zhidu30.xinhuimed.net/api/v3/login'
# header = {
#     'Content-Type':'application/json'
#
# }
#
# json = {
#     'username': 'J/fY3PE2HH0kvMZzbv5BLQ==',
#     'password': 'ez27Us6DpzGoPNkb3FH/Mw==',
#     'captcha': '',
#     'captcha_code': '6666',
#     'captcha_key': '$2y$10$reArgS92v9zKSj.Z77yls.nqw0mxi1gVyEVzu.eYv9vT6/2DS8Z9q',
#     'type': 'username',
#     'mobile':'',
#     'sms_code':''
# }
#
#
# response1 = se.post(url=url1,json=json,headers=header)
# #
# # print(response1.json())
# # print("这是status_code：{}\n".format(response1.status_code))
# #
# # print("这是cookies：.{}\n".format(response1.cookies))
# #
# # print("这是headers：.{}\n".format(response1.headers))
# #
# # print("这是url：.{}\n".format(response1.url))
#
# response = se.get(url= 'http://xh-test.zhidu30.xinhuimed.net/api/v3/setting/config')
#
# # response1 = requests.get(url='http://xh-test.zhidu30.xinhuimed.net/api/v3/regulation',params={})
#
# print(response.status_code)
#
# print(response1.json())
# # print("这是status_code：{}\n".format(response.status_code))
# #
# # print("这是cookies：.{}\n".format(response.cookies))
# #
# # print("这是headers：.{}\n".format(response.headers))
# #
# # print("这是url：.{}\n".format(response.url))
#
# print("这是响应页面文本信息：.{}\n".format(response.text))   # 因为返回数据太长，不作运行
# print("这是获取的字节流数据decode解码：.{}\n".format(response.content.decode()))
