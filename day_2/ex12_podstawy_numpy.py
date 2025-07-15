import math

import numpy as np

# pip install numpy

# ndarray - tablice, macierze
array = np.array([10, 100, 1000.])
print(array)  # [  10.  100. 1000.]

array2 = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(array.dtype)  # float64

# rzutowanie na float pythonowy
print(float(array[0]))  # 10.0

# rozglaszanie i wektoryzacja obliczen
print(array2 + 1)
# [[2 3 4]
#  [5 6 7]]
print(array2 * array2)
# [[ 1  4  9]
#  [16 25 36]]

# print(math.sqrt(array2)) # TypeError: only length-1 arrays can be converted to Python scalars

print(np.sqrt(array2))
# [[1.         1.41421356 1.73205081]
#  [2.         2.23606798 2.44948974]]
print(array2.sum())  # 21
