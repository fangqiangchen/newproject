from pygopus import WorkBook

book = WorkBook("./Day3/users.xlsx")
sh = book.get_sheet("Sheet1")

for index,row in enumerate(sh.rows):
    if "失效" in row:
        print(row)
        sh.delete_row(index+1)
    book.save()


