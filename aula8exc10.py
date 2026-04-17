import numpy as np

# 10) Soma dos 20 primeiros termos da série de Taylor de sin(x)
# Observação: a fórmula não apareceu inteira no texto extraído do PDF,
# então usei a expansão mais comum de Taylor para sin(x):
# sin(x) = x - x^3/3! + x^5/5! - ...


def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat


def taylor_sin(x, termos=20):
    soma = 0
    for n in range(termos):
        soma += ((-1) ** n) * (x ** (2*n + 1)) / fatorial(2*n + 1)
    return soma


x = 1.0
print("Aproximação de sin(1):", taylor_sin(x, 20))
print("Valor do numpy:", np.sin(x))
