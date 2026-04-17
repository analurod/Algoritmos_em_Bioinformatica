# 6) Recebe uma lista e retorna a soma dos quadrados

def soma_quadrados(lista):
    soma = 0
    for num in lista:
        soma += num ** 2
    return soma


numeros = [1, 2, 3, 4]
print("Soma dos quadrados:", soma_quadrados(numeros))
