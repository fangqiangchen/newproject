import os
import xlwt
file_dir = '/Users/chenfangqiang/Downloads'

os.listdir(file_dir)

new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet('new_test')
n = 0
for i in os.listdir(file_dir):
    worksheet.write(n,0,i)
    n += 1
new_workbook.save('/Users/chenfangqiang/Downloads/CourseCode/S1/1-2/LessonCode/file_name.xls')