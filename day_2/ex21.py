# xlwt - zapis do plikow xls
import xlwt

# pip install xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Dane")

sheet.write(0, 0, "Imie")
sheet.write(0, 1, "Wiek")
sheet.write(1, 0, "Jan")
sheet.write(1, 1, 28)

workbook.save("plik_xlwt.xls")
