import numpy as np

# 5) Acessos no array

a = np.array([[10, 20, 30], [40, 50, 60]])

# a) elemento da 2ª linha e 3ª coluna
print(a[1, 2])

# b) primeira linha inteira
print(a[0])

# c) todos os elementos da coluna 2
print(a[:, 1])
