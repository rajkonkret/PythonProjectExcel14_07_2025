import time
import numpy as np

lista = list(range(15_000_000))
lista_np = np.arange(15_000_000, dtype=np.int64)


# deklaracja funkcji
def sum_python():
    total = 0
    for i in lista:
        total += i
    print("Sum is:", total)


def sum_np():
    total = np.sum(lista_np)
    print("Sum is:", total)


start_d = time.time()
sum_python()  # uruchomienie funkcji
end_d = time.time()
print(end_d - start_d)

start_d = time.time()
sum_np()  # uruchomienie funkcji
end_d = time.time()
print(end_d - start_d)
# Sum is: 112499992500000
# 0.2068042755126953
# Sum is: 112499992500000
# 0.006269216537475586