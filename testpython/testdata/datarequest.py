def login_check(username,password,code,key,type1):

    json1 = {
        'username': username,
        'password': password,
        'captcha': '',
        'captcha_code': code,
        'captcha_key': key,
        'type': type1,
        'mobile': '',
        'sms_code': ''}

    return json1