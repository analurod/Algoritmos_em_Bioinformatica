# Escreva um programa que simule um caixa eletrônico,
# solicitando ao usuário que insira o valor do saque e informando
# quantas notas de cada valor serão entregues (considere notas
# de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2).

num = int(input())

resto = num

cem = resto // 100
resto = resto % 100

cinq = resto // 50
resto = resto % 50

vint = resto // 20
resto = resto % 20

dez = resto // 10
resto = resto % 10

cinco = resto // 5
resto = resto % 5

dois = resto // 2
resto = resto % 2

print(f'Notas de R$100,00: {cem}')
print(f'Notas de R$50,00: {cinq}')
print(f'Notas de R$20,00: {vint}')
print(f'Notas de R$10,00: {dez}')
print(f'Notas de R$5,00: {cinco}')
print(f'Notas de R$2,00: {dois}')
