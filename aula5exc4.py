# 4) Leia 20 números inteiros e separe em pares e ímpares

numeros = []
pares = []
impares = []

for i in range(20):
    n = int(input(f"Digite o número inteiro: "))
    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Todos os números:", numeros)
print("Pares:", pares)
print("Ímpares:", impares)
