import xlrd,xlwt
#读取制定表数据
xlsx = xlrd.open_workbook('/Users/chenfangqiang/PycharmProjects/newproject/CourseCode/Chapter1/S1-1-1/PracticeNeed/7月下旬入库表.xlsx')
table = xlsx.sheet_by_index(0)

print(table.cell_value(1,2))
print(table.cell(1,2).value)
print(table.row(1)[2].value)
#写入新表单
new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet('new_test')
worksheet.write(0,0,'test')
new_workbook.save('/Users/chenfangqiang/PycharmProjects/newproject/CourseCode/Chapter1/S1-1-1/PracticeNeed/text1.xls')