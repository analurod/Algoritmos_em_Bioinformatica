# Crie um programa que determine se um número é um
# número de Armstrong ou não. Um número de Armstrong é
# aquele que é igual à soma de seus dígitos elevados à potência
# do número de dígitos.

num = input()
tam = len(num)
soma = 0

for i in range(0, tam):
    soma = soma + int(num[i])**tam

if soma == int(num):
    print('É número de Armstrong')
else:
    print('Não é número de Armstrong')
