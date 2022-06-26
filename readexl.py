import xlrd
 
loc = ("c://ecp/test.xls")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
 
for i in range(sheet.nrows):
    if i != 0:
        print(sheet.cell_value(i, 2))
    