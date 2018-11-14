# import os
# # ls = [s for s in range(101) if (s%2 != 0)]
# # print(ls)
# a = [d for d in os.listdir('.')]
# print(a)
import xlrd
import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet('test')
sheet.write(0,0,'test')
book.save('test.xls')