from testpython.data.openxl import ReadExcel

excel = ReadExcel('test.xlsx', 'Sheet')
cases = excel.read_data()
print(cases)