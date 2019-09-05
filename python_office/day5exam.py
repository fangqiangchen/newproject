import xlwt,xlrd
import random
from xlutils.copy import copy
#读取工作薄
xlsx = xlrd.open_workbook('/Users/chenfangqiang/Downloads/CourseCode/S1/1-2/LessonCode/日统计.xls',formatting_info=True)
#打开工作表
table = xlsx.sheet_by_index(0)
#复制一个新工作薄
new_xlsx = copy(xlsx)
#获取工作表数据
new_sheet= new_xlsx.get_sheet(0)
#样式初始化
style = xlwt.XFStyle()
#初始化字体
font = xlwt.Font()
#设置字体样式
font.name = '宋体'
font.bold = True
font.height = 360
#导入字体样式
style.font = font
#设置边框样式
borders = xlwt.Borders()
#设置边框样式
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
#导入边框样式
style.borders = borders
#设置文字位置
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
#导入对齐方式
style.alignment = alignment
#样式初始化红色
style_red = xlwt.XFStyle()
#初始化字体
font_red = xlwt.Font()
#设置字体样式
font_red.name = '宋体'
font_red.bold = True
font_red.height = 360
font_red.colour_index = 2
#导入字体样式
style_red.font = font_red
#设置边框样式
borders_red = xlwt.Borders()
#设置边框样式
borders_red.top = xlwt.Borders.THIN
borders_red.bottom = xlwt.Borders.THIN
borders_red.left = xlwt.Borders.THIN
borders_red.right = xlwt.Borders.THIN
#导入边框样式
style_red.borders = borders_red
#设置文字位置
alignment_red = xlwt.Alignment()
alignment_red.horz = xlwt.Alignment.HORZ_CENTER
alignment_red.vert = xlwt.Alignment.VERT_CENTER
#导入对齐方式
style_red.alignment = alignment

stylex = lambda x : style_red if x >10 else style
#写入数据
for i in range(2,6):
    a = random.randint(0, 50)
    new_sheet.write(i,1,a,stylex(a))
new_xlsx.save('/Users/chenfangqiang/Downloads/CourseCode/S1/1-2/LessonCode/日统计1.xls')