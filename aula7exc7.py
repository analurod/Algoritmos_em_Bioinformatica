# 7) Calculadora com *args

def produto_total(*numeros):
    produto = 1
    for num in numeros:
        produto *= num
    return produto


print(produto_total(2, 3))
print(produto_total(2, 3, 4))
print(produto_total(1, 2, 3, 4, 5))
