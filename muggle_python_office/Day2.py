from pygopus import WorkBook

book = WorkBook("./Day1/orders.xlsx")
sh = book.get_sheet("this")
list = []
for row in sh.rows:
    if "面膜 x 1" in row:
        list.append(row)

new_book = WorkBook("./Day1/facemask.xlsx","w+")
sheet = new_book.get_sheet("Sheet1")
sheet.write_rows(list)
new_book.save()

