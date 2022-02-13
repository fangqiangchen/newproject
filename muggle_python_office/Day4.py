from pygopus import WorkBook
import os
files = os.listdir("./Day4/files")
for f in files:
    path = "./Day4/files/" + f
    book = WorkBook(path)
    shs = book.sheets
    for sh in shs:
        if "最终" in sh.name:
            book.save_as("我要找的.xlsx")


# book = WorkBook("./Day4/files/导出数据.xlsx")
# shs = book.sheets
# for sh in shs:

