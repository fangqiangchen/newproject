from pygopus import WorkBook

orders_book = WorkBook("./Day5/orders.xlsx")
tpl_book = WorkBook("./Day5/tpl.xlsx")
orders_sh = orders_book.get_sheet("this")
tpl_sh = tpl_book.get_sheet("Sheet1")

for row in orders_sh.rows:
    tpl_sh.batch_set("A2","A3","A4","A5","A6",data=row)
    file_name = "./Day5/outputs/" + row[0] + ".xlsx"
    tpl_book.save_as(file_name)

