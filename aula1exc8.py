#  Crie um programa que calcule o tempo de viagem, pedindo
# ao usuário a distância e a velocidade.

km = float(input('Digite a distância em km: '))
velocidade = float(input('Qual velocidade: '))

km_hora = km / velocidade

print(f'A sua viagem de {km: 4.2f} km a uma velocidade de {
      velocidade: 4.2f}km/h irá durar {km_hora: 4.2f} horas')
