from pygopus import WorkBook

book = WorkBook("./Day6/emp2.xlsx")

sh = book.get_sheet("Sheet1")
# 从正数第二个开始
for row in sh.rows[1:]:
    if int(row[2]) > 1000:
        row.highlight()
        if row[-1].endswith("1212"):
            row.highlight(at=0, color="#ABEBC6")
print("Done")
book.save()
