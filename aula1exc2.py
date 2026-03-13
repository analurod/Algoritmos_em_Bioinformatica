# Escreva um script que leia um valor em metros e o exiba
# convertido em milímetros

metros = float(input('Digite um valor em metros: '))

mm = metros * 1000

print(f'{metros}m é equivalente a {mm: 4.2f} mm.')
