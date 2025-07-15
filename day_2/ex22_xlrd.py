import xlrd  # do odczytu plikow xls

# pip install xlrd

workbook = xlrd.open_workbook('../data/plik_xlwt.xls')
sheet = workbook.sheet_by_index(0)

print(sheet.cell_value(0, 0))
print(sheet.cell_value(1, 0))
# Imie
# Jan