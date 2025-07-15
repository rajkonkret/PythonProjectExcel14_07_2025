import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [4, 5, 6, 7]})
print(df)
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6
# 3  4  7

print(df.describe())
# count  4.000000  4.000000
# mean   2.500000  5.500000
# std    1.290994  1.290994
# min    1.000000  4.000000
# 25%    1.750000  4.750000
# 50%    2.500000  5.500000
# 75%    3.250000  6.250000
# max    4.000000  7.000000

df.plot.box()
plt.show()
# https://colab.research.google.com/drive/1o_PVAm5HCgfx_VpwLzPMX1JTrJKZ8z0c#scrollTo=o6pq-VpRGzyj
