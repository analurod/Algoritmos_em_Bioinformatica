# Faça um Programa que leia uma lista de 10 números reais e mostre-
# os na ordem inversa.

numeros = []
for i in range(10):
    n = float(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

print("Ordem inversa:", numeros[::-1])
