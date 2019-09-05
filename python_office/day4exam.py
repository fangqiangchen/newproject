import xlrd,xlwt
#定义工作薄位置
xlsx = xlrd.open_workbook('/Users/chenfangqiang/Downloads/CourseCode/S1/1-1/LessonCode/7月下旬入库表.xlsx')
#创建新工作薄
new_workbook = xlwt.Workbook()
#创建新工作薄新工作表
worksheet = new_workbook.add_sheet('new_7月下旬入库表')
#读取工作工作表
table = xlsx.sheet_by_index(0)
#for循环读取就数据表数据
#坑一把table.nrows,写成了xlsx.nrows导致找不到数据
for r in range(0,table.nrows):
    for l in range(0,table.ncols):
#写入数据
#坑2把table.cell_value写成了xlsx.cell.value导致报错
        worksheet.write(r,l, table.cell_value(r,l))
        print(table.cell_value(r,l))
#保存工作薄地址
new_workbook.save('/Users/chenfangqiang/Downloads/CourseCode/S1/1-1/LessonCode/new_7月下旬入库表.xlsx')