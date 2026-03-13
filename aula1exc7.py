#  Leia o valor de um produto e calcule o valor final com 10% de
# desconto.

valor = float(input('Digite o valor do produto: '))
valordesc = valor - (valor * 0.1)

print(f'O valor com 10% de desconto é {valordesc:4.1f}')
