# Crie uma função mylog que calcule ln (1+x) usando 30 termos de Mercator (valida para |x|<1):
# ln(1+x) = somatorio (-1)^(n+1) * x^n / n, para n= 1, 2, ..., 30. Não usar for ou while. usenumpy e numpy.arnage

import numpy as np


def mylog(x):
    if abs(x) >= 1:
        return "Erro: a série de Mercator vale para |x| < 1"

    n = np.arange(1, 31)
    return np.sum(((-1)**(n+1)) * (x**n) / n)


x = float(input("Insira o x: "))
resultado = mylog(x)
print(f'O resultado é {resultado}')
