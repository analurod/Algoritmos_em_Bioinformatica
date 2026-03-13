# Faça um script que calcule o aumento de salário. Ele deve
# solicitar o valor do salário e a porcentagem de aumento.
# Exiba o valor do aumento e do novo salário.

print("-------------------------------")
print("CALCULE SEU AUMENTO DE SALÁRIO!")
print("-------------------------------")

salario = float(input('Digite seu salário atual: '))
percentual = float(input('Digite o percentual de aumento: '))
aumento = (salario * percentual/100)
salarionovo = salario + aumento


print(f'Seu salário atual: R${salario: 4.2f} com {percentual: 4.1f}% de aumento resulta em um aumento de R${
      aumento: 4.2f}. Seu novo salário será R${salarionovo: 4.2f}')
