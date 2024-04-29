
#
# a = 1
#
# try:
#     a = 1
#     print(b)
# #
# # except(NameError,FileNotFoundError):
# #     print('这是个异常')
# #
#
# except Exception as msg:
#
#     print('这是个异常')



try:
    score = int(input("请输入成绩"))

except Exception as msg:

    print('输入不正确默认给0分')
    score = 0
    # raise msg

else:
    print('输入成功')


finally:
    print('成绩为{}'.format(score))




