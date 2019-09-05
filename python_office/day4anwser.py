import xlrd, xlwt

xlsx = xlrd.open_workbook('/Users/chenfangqiang/Downloads/CourseCode/S1/1-1/LessonCode/7月下旬入库表.xlsx')
table = xlsx.sheet_by_index(0)
newworkbook= xlwt.Workbook()
worksheet = newworkbook.add_sheet('new_7月下旬入库表')
for x in range(0,table.nrows):
    for y in range(0,table.ncols):
        if table.cell(x,y).ctype == 3:
            datecell = xlrd.xldate.xldate_as_datetime(table.cell(x,y).value,0)

            values = datecell.strftime('%Y/%m/%d')
            worksheet.write(x,y,values)
        else:
            values = table.cell(x,y).value
            worksheet.write(x,y,values)
newworkbook.save('/Users/chenfangqiang/Downloads/CourseCode/S1/1-1/LessonCode/new_7月下旬入库表.xlsx')
