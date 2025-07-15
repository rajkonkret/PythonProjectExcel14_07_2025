import openpyxl
from openpyxl.chart import Reference, BarChart

wb = openpyxl.load_workbook('videogamesales2.xlsx')

ws = wb['Total Sales by Genre']

values = Reference(ws,
                   min_col=2,
                   max_col=2,
                   min_row=1,
                   max_row=13)

cats = Reference(ws,
                 min_col=1,
                 max_col=1,
                 min_row=2,
                 max_row=13)

chart = BarChart()
chart.add_data(values, titles_from_data=True)
chart.set_categories(cats)
chart.title = "Total Sales"
chart.x_axis.title = "Genre"
chart.y_axis.title = "Total Sales by Genre"

ws.add_chart(chart, "D2")

wb.save("videogamesales2.xlsx")
wb.close()
