# Crie um programa que calcule o IMC (Índice de Massa
# Corporal) de uma pessoa e forneça uma classificação com
# base no resultado.

peso = float(input('peso: '))
altura = float(input('altura: '))

imc = peso / (altura**2)

print(imc)

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Normal')
elif imc >= 25 and imc < 29.9:
    print('Sobrepeso')
else:
    print('Obesidade')
