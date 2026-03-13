#  Escreva um programa que calcule o IMC (Índice de Massa
# Corporal) de uma pessoa.
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso/(altura**2)

print(f'Seu IMC é {imc:4.1f}')
