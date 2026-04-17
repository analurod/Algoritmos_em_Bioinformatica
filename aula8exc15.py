import numpy as np

# 15) Concatenar dois arrays 1D de 5 elementos

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

c = np.concatenate((a, b))
print(c)
