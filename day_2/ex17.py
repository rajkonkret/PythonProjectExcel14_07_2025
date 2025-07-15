import pandas as pd

height_data = [
    {"Name": "Aditya", "Height": 179},
    {"Name": "Sammer", "Height": 181},
    {"Name": "Darwin", "Height": 170},
    {"Name": "Anna", "Height": 167},
]
weight_data = [
    {"Name": "Aditya", "Weight": 79},
    {"Name": "Sammer", "Weight": 81},
    {"Name": "Darwin", "Weight": 70},
    {"Name": "Anna", "Weight": 73},
]

marks_data = [
    {"Name": "Aditya", "Marks": 179},
    {"Name": "Sammer", "Marks": 181},
    {"Name": "Darwin", "Marks": 170},
    {"Name": "Anna", "Marks": 173},
]

height_data_df = pd.DataFrame(height_data)
weight_data_df = pd.DataFrame(weight_data)
marks_data_df = pd.DataFrame(marks_data)

writer = pd.ExcelWriter("../data/excel_with_multiple_sheets.xlsx", engine='xlsxwriter')

height_data_df.to_excel(writer, sheet_name="height", index=False)
weight_data_df.to_excel(writer, sheet_name="weight", index=False)
marks_data_df.to_excel(writer, sheet_name="marks", index=False)

writer.close()
