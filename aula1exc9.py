#  Escreva um script que pergunte a quantidade de km
# percorridos por um carro alugado pelo usuário e a
# quantidade de dias pelo qual o carro foi alugado. Calcule o
# preço a pagar sabendo que o carro custa 60 reais por dia e
# 15 centavos por Km rodado.

km = float(input('Digite a distância percorrida em km: '))
dias = int(input('Digite a quantidade de dias que o carro ficou alugado:  '))

valor = (60 * dias) + (0.15 * km)

print(f'O aluguel do carro por {dias} dias, com {
      km: 4.2f} km percorridos irá custar R$ {valor: 4.2f}')
