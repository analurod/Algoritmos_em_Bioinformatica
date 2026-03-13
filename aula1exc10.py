#  A resistência combinada de três resistores R1, R2 e R3 em
# paralelo é dada por

# R = 1 / (1/R1 + 1/R2 + 1/R3)

# Crie três variáveis com três valores de resistências e calcule a
# resistência resultante.

r1 = float(input('Digite a resistência do 1º resistor: '))
r2 = float(input('Digite a resistência do 2º resistor: '))
r3 = float(input('Digite a resistência do 3º resistor: '))

resistencia = 1 / (1/r1 + 1/r2 + 1/r3)

print(f'A resistência resultante é {resistencia: 4.2f} ohm')
