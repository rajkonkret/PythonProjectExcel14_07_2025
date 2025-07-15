import pandas as pd

df = pd.read_csv("../data/height_file.csv")
print(df)
#        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167

writer = pd.ExcelWriter("../data/excel_from_csv.xlsx", engine="xlsxwriter")

df.to_excel(writer, sheet_name="first_sheet", index=False)
writer.close()
