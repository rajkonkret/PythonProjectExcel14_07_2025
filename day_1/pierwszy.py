# Pep8 - https://peps.python.org/pep-0008/
import sys

print()  # wypisz/wydrukuj
# ctrl alt l - formatowanie kodu

print("Radek")
print('Radek')

# crtrl / - komentarz
# Radek
# Radek
# print("Radek')
#   File "C:\Users\Szkolenie\PycharmProjects\PythonProjectExcel14_07_2025\day_1\pierwszy.py", line 11
#     print("Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 11)
print('Dalej')  # Dalej

# type()
print(type('Radek'))  # <class 'str'> - tekstowy
# konkatenacja, łączenie tekstów
print("39" + "14")  # 3914
print(39 + 14)  # 53
print(type(39))  # <class 'int'> - liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#             default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# zmienna - pudełko na dane
# przechowuje jeden element

# typowanie dynamiczne
name = "Radek"
print(type(name))  # <class 'str'>
print(name)  # Radek

name = 90
print(type(name))
print(name)

# hint - podpowiedź
name: str = "Radek"
print(name)
print(type(name))  # 90
# mypy
#  pip install mypy
#  cd .\day_1\
#  mypy .\pierwszy.py
name = 90
print(name)

tekst = "Witaj Świecie"

# teksty są niemutowalne
print(tekst)
print(type(tekst))
tekst.upper()
print(tekst)  # Witaj Świecie
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE
zmienna = tekst.upper()
print(zmienna)  # WITAJ ŚWIECIE

zmienna1 = "GROSS"
zmienna2 = "groß"

print(zmienna1.lower() == zmienna2.lower())  # False
# casefold() - sprawdza z uwzględnieniem problemu ß
print(zmienna1.casefold() == zmienna2.casefold())  # True
# == porównanie

print(1 != 0)  # True - czy różne

# rzutowanie - zamiana
print(int("39"))  # 39 rzutowanie na int
print(str(39))  # rzutowanie na str

# print("14" + 39)  # TypeError: can only concatenate str (not "int") to str
print("14" + str(39))  # 1439

temp = 36.6
print(type(float))  # <class 'type'>, zmiennoprzecinkowe
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#
#                max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004
# float posiada błąd zaokrąglenie
# decimal - pozwala ominąć problem błedu zaokrąglenia - więcej pamięci, wolniejsze obliczenia

# f - string, string sformaty
name = "Radek"
print(f"Nazywam się {name}")  # Nazywam się Radek
print("Nazywam się {}".format(name))  # Nazywam się Radek

print("Nazywam się %s" % name)  # NAzywam się Radek
"""
Komentarz
    wielolinijkowy"""

print("""Tekst
    wielolinijkowy""")

# "Tekst
#     wielolinijkowy"

print(100 / 2.2)  # 45.45454545454545
print(100 // 2.2)  # 45.0 - czesc całkowita
print(100 % 2.2)  # 0.999999999999992 reszta z dzielenia

print(10 % 3)  # reszta 1, modulo

zysk = 890123456765
# ctrl d - powielenie lini
print(f"Nasza duża liczba: {zysk}")  # Nasza duża liczba: 890123456765
print(f"Nasza duża liczba: {zysk:,}")  # Nasza duża liczba: 890,123,456,765
print(f"Nasza duża liczba: {zysk:,}".replace(",", " "))  # Nasza duża liczba: 890 123 456 765
print(f"Nasza duża liczba: {zysk:,}".replace(",", "."))  # Nasza duża liczba: 890.123.456.765

zysk = 890_123_456_765
print(type(zysk))
print(zysk)  # 890123456765

encoded_text = tekst.encode('utf-8')
print(encoded_text)  # b'Witaj \xc5\x9awiecie' typ bajtowy
print(type(encoded_text))  # <class 'bytes'>
print(encoded_text.decode('utf-8'))  # Witaj Świecie

# typ logiczny
print(True)
print(False)

# kolekcje
# lista, krotka(tupla), zbior(set), słownik

lista = [5, 6, 7, 8, 9, "Radek"]
print(lista)  # [5, 6, 7, 8, 9, 'Radek']
lista.append("Ewa")
print(lista)  # [5, 6, 7, 8, 9, 'Radek', 'Ewa']
lista.remove("Radek")
print(lista)  # [5, 6, 7, 8, 9, 'Ewa']

lista2 = lista  # kopia referencji
print(lista)  # [5, 6, 7, 8, 9, 'Ewa']
print(lista2)  # [5, 6, 7, 8, 9, 'Ewa']
lista.remove(9)
print(lista)  # [5, 6, 7, 8, 'Ewa']
print(lista2)  # [5, 6, 7, 8, 'Ewa']

lista_copy = lista.copy()  # skopiowanie elementów listy do innej
print(lista)
print(lista_copy)
lista_copy.append("Radek")
print(lista)  # [5, 6, 7, 8, 'Ewa']
print(lista_copy)  # [5, 6, 7, 8, 'Ewa', 'Radek']

# krotka - tupla - lista do odczytu
krotka = tuple(lista_copy)
print(krotka)  # (5, 6, 7, 8, 'Ewa', 'Radek') - pozwala efektywniwj zarzadzac pamięcią

# zbiór
zbior = {5, 6, 5, 6, 6, 7, 8, 9, 0}  # przechowuje unikalne wartości
print(zbior)  # {0, 5, 6, 7, 8, 9}
# nie zachowuje kolejnoci

slownik = {"name": "Radek", "age": 56}
print(slownik)  # {'name': 'Radek', 'age': 56}
slownik2 = {"name": ["Radek", "Tomek", "Piotr"]}
print(slownik2)
# {'name': ['Radek', 'Tomek', 'Piotr']}
print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_keys(['name', 'age'])
# dict_values(['Radek', 56])
# dict_items([('name', 'Radek'), ('age', 56)])
