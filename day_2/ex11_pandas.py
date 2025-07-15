import pandas as pd

# pip install pandas
#

writer = pd.ExcelWriter('../data/empty_file.xlsx')
empty_dataframe = pd.DataFrame()
empty_dataframe.to_excel(writer, sheet_name='empty')
writer.close()
