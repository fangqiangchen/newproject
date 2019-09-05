from xlutils.copy import copy
import xlrd,xlwt
#打开工作薄
tem_excel = xlrd.open_workbook('/Users/chenfangqiang/Downloads/CourseCode/S1/1-2/LessonCode/日统计.xls', formatting_info=True)
#打开工作表
tem_sheet = tem_excel.sheet_by_index(0)
#复制旧表
new_excel = copy(tem_excel)
#打开新工作薄第一个工作表
new_sheet = new_excel.get_sheet(0)
#设置样式
style = xlwt.XFStyle()
#设置字体
font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
font.height = 360
style = xlwt.XFStyle()

font = xlwt.Font()
font.name = '宋体'
font.bold = True
font.height = 360
style.font = font
#添加字体到样式
style.font = font
#初始化边框
borders = xlwt.Borders()
#添加边框
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
#添加边框到样式
style.borders = borders
#初始化对齐
alignment = xlwt.Alignment()
#对齐方式
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
#写入对齐
style.alignment = alignment
#写入数据
new_sheet.write(2,1,12)
new_sheet.write(3,1,15)
new_sheet.write(4,1,12)
new_sheet.write(5,1,18)
new_excel.save('/Users/chenfangqiang/Downloads/CourseCode/S1/1-2/LessonCode/填写.xls')
