import xlrd
import xlwt
from xlutils.copy import copy
def write(row_num,value):
    read = xlrd.open_workbook('成绩单.xls')
    table = copy(read)
    get_table = table.get_sheet(0)
    get_table.write(row_num,2,value)
    table.save('成绩单.xls')