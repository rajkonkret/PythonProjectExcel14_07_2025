import pandas as pd

df = pd.read_excel("../data/excel_with_multiple_sheets.xlsx", sheet_name=2)
# 2 arkusz numer 3
print("The dataframe is:")
print(df)
# The dataframe is:
#      Name  Marks
# 0  Aditya    179
# 1  Sammer    181
# 2  Darwin    170
# 3    Anna    173

df = pd.read_excel("../data/excel_with_multiple_sheets.xlsx", sheet_name="marks")
print("The dataframe is:")
print(df)
#      Name  Marks
# 0  Aditya    179
# 1  Sammer    181
# 2  Darwin    170
# 3    Anna    173

# aby odczytac nazwy arkuszy w pliku nalezy uzyc ExcelFile
dane = pd.ExcelFile("../data/excel_with_multiple_sheets.xlsx")
print(dane.sheet_names)  # ['height', 'weight', 'marks']

df = pd.read_excel("../data/excel_with_multiple_sheets.xlsx", sheet_name=dane.sheet_names[0])
print("The dataframe is:")
print(df)
# The dataframe is:
#      Name  Height
# 0  Aditya     179
# 1  Sammer     181
# 2  Darwin     170
# 3    Anna     167

# wczytanie konkretnej tabeli
df = pd.read_excel("../data/excel_with_multiple_sheets.xlsx", sheet_name="marks", usecols=['Name'])
print("The dataframe is:")
print(df)
#      Name
# 0  Aditya
# 1  Sammer
# 2  Darwin
# 3    Anna
