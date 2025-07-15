import pandas as pd

df = pd.DataFrame({
    "Imie": ["Anna", "Tomek", "Jan", "Anna", "Jan"],
    "Miasto": ['Kraków', "Warszawa", "Gdańsk", "Kraków", "Gdańsk"],
    "Wynik": [88, 95, 70, 91, 60]
})

df_sorted = df.sort_values(by="Imie")
print(df_sorted.head)

# malejąco
df_sorted_desc = df.sort_values(by="Imie", ascending=False)
print(df_sorted_desc)
# 1  Tomek  Warszawa
# 2    Jan    Gdańsk
# 4    Jan    Gdańsk
# 0   Anna    Kraków
# 3   Anna    Kraków

df_sorted_multi = df.sort_values(by=['Miasto', 'Wynik'], ascending=[True, False])
print(df_sorted_multi)
#     Imie    Miasto
# 1  Tomek  Warszawa
# 2    Jan    Gdańsk
# 4    Jan    Gdańsk
# 0   Anna    Kraków
# 3   Anna    Kraków

df_grouped_mean = df.groupby("Imie", as_index=False)['Wynik'].mean()
print(df_grouped_mean)
#     Imie  Wynik
# 0   Anna   89.5
# 1    Jan   65.0
# 2  Tomek   95.0

df_grouped_sum = df.groupby("Imie", as_index=False)['Wynik'].sum()
print(df_grouped_sum)
#     Imie  Wynik
# 0   Anna    179
# 1    Jan    130
# 2  Tomek     95

df_groped_count = df.groupby("Imie").size().reset_index(name="Ilość wpisów")
print(df_groped_count)
#     Imie  Ilość wpisów
# 0   Anna             2
# 1    Jan             2
# 2  Tomek             1

with pd.ExcelWriter('raport.xlsx', engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Oryginalne", index=False)
    df_sorted.to_excel(writer, sheet_name="Posortowane", index=False)
    df_grouped_mean.to_excel(writer, sheet_name="Średnia", index=False)
