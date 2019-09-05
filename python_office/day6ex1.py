import xlwt,xlrd
from xlutils.copy import copy
#打开工作薄
xlsx = xlrd.open_workbook('/Users/chenfangqiang/Downloads/CourseCode/S1/1-3/LessonCode/7月下旬入库表.xlsx')
#打开工作表
table = xlsx.sheet_by_index(0)
#存储取出数据
all_data =[]

for n in range(1,table.nrows):
    company = table.cell(n, 1).value
    price = table.cell(n, 3).value
    weight = table.cell(n, 4).value
    data = {'company': company, 'price': price, 'weight': weight}
    all_data.append(data)
#列表存储数据
a_weight = []
a_total_price = []
b_weight = []
b_total_price = []
c_weight = []
c_total_price = []
d_weight = []
d_total_price = []
#存储数据到列表
for i in all_data:
    if i['company'] == '张三粮配':
        a_weight.append(i['weight'])
        a_total_price.append(i['weight'] * i['price'])
    if i['company'] == '李四粮食':
        b_weight.append(i['weight'])
        b_total_price.append(i['weight'] * i['price'])
    if i['company'] == '王五小麦':
        c_weight.append(i['weight'])
        c_total_price.append(i['weight'] * i['price'])
    if i['company'] == '赵六麦子专营':
        d_weight.append(i['weight'])
        d_total_price.append(i['weight'] * i['price'])
#复制一份工作表
tem_excel = xlrd.open_workbook('/Users/chenfangqiang/Downloads/CourseCode/S1/1-3/LessonCode/7月下旬统计表.xls')
tem_sheet = tem_excel.sheet_by_index(0)

new_excel = copy(tem_excel)
new_sheet = new_excel.get_sheet(0)

style = xlwt.XFStyle()

font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
font.height = 16 * 20
style.font = font

borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment

new_sheet.write(2,1,len(a_weight),style)
new_sheet.write(2,2,round(sum(a_weight),2),style)
new_sheet.write(2,3,round(sum(a_total_price),2),style)
new_sheet.write(3,1,len(a_weight),style)
new_sheet.write(3,2,round(sum(a_weight),2),style)
new_sheet.write(3,3,round(sum(a_total_price),2),style)
new_sheet.write(4,1,len(a_weight),style)
new_sheet.write(4,2,round(sum(a_weight),2),style)
new_sheet.write(4,3,round(sum(a_total_price),2),style)
new_sheet.write(5,1,len(a_weight),style)
new_sheet.write(5,2,round(sum(a_weight),2),style)
new_sheet.write(5,3,round(sum(a_total_price),2),style)

new_excel.save('/Users/chenfangqiang/Downloads/CourseCode/S1/1-3/LessonCode/7月下旬统计表1.xls')




