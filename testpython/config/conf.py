from configparser  import ConfigParser


class Mycong():


    def __init__(self,file_name,encoding='utf8'):
        self.file = file_name
        self.encoding = encoding
        self.conf = ConfigParser()
        self.conf.read(self.file,self.encoding)


    def get_int(self,section,option):
        return self.conf.getint(section,option)

    def get_str(self,section,option):
        return self.conf.get(section,option)

    def get_items(self,section):
        return self.conf.items(section)

    def get_float(self):
        pass

    def write_data(self,section,option,value):
        self.conf.add_section(section)
        self.conf.set(section, option, value)
        self.conf.write(self.file,'a',self.encoding)


# if __name__ =='__main__':










































'''
conf = ConfigParser()

conf.read('env.ini',encoding='utf8')

res1 = conf.sections()

print('这是res1：{}\n'.format(res1))

res2 = conf.options('loggin')

print('这是res2：{}\n'.format(res2))

res3 = conf.items('loggin')

print('这是res2：{}\n'.format(res3))

res5 = conf.get("loggin", "le1")
print("这是res5：{}".format(res5), type(res5))
# getint方法：读取出来的内容，都是int类型
res6 = conf.getint("mysql", "port")
print("\n这是res6：{}".format(res6), type(res6))


conf = ConfigParser()
conf.add_section('test')
conf.set('test', 'name', 'Amy')
conf.write(open('env.ini', "a", encoding="utf-8"))

'''

