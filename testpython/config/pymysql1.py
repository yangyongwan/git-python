from testpython.config.conf import Mycong
import pymysql

class PymysqlData:
    def __init__(self,filename):
        self.data = Mycong(filename)
        self.con = pymysql.connect(host = self.data.get_str('mysql','host'),
                      user=self.data.get_str('mysql','username'),
                      password=self.data.get_str('mysql','password'),
                      port=self.data.get_int('mysql','port'),
                      charset='utf8'
        )

        self.cur = self.con.cursor()
        self.cur.execute(self.data.get_str('mysql','library'))

    def get_one(self,sql):
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all(self,sql):
        self.cur.execute(sql)
        columns = [desc[0] for desc in self.cur.description]
        result = self.cur.fetchall()
        cases = []
        for i in result:
            case = []
            for n in i:
                case.append(n)
            cases.append(dict(zip(columns, case)))
        return cases
    def get_count(self,sql):
        self.con.commit()
        self.cur.execute(sql)
        self.data_count = len(self.cur.fetchall())
        return self.data_count
    def close(self):
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    sql = 'SELECT * FROM users WHERE org_id = 1722'
    database = PymysqlData('env.ini')
    data_count = database.get_count(sql)
    print(data_count)
    data_t = database.get_all(sql)
    print(data_t)



















# data = Mycong('env.ini')
# # data_list = data.get_items('mysql')
# # print(data_list)
#
# con = pymysql.connect(host = data.get_str('mysql','host'),
#                       user=data.get_str('mysql','username'),
#                       password=data.get_str('mysql','password'),
#                       port=data.get_int('mysql','port'),
#                       charset='utf8'
# )
#
# cur =con.cursor()
# cur.execute('USE xh')
# sql = 'SELECT * FROM users WHERE org_id = 1722'
# res = cur.execute(sql)
#
# columns = [desc[0] for desc in cur.description]
# print(columns)
# #
#
# result = cur.fetchall()
# print(result)
# cases = []
# # case = []
# for i in result:
#     case = []
#     for n in i:
#         case.append(n)
#     cases.append(dict(zip(columns,case)))
# print(cases)
#
# for j in cases:
#     print(j)
