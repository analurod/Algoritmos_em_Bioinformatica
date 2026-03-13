# Escreva um script que leia a quantidade de dias,horas,
# minutos e segundos para o usuário. Calcule o total em
# segundos.

horas = float(input('Digite as horas: '))
minutos = float(input('Digite os minutos: '))
segundos = metros = float(input('Digite os segundos: '))

segfinal = segundos + (minutos*60) + (horas*3600)

print(f'{horas: 4.2f} hora(s), {minutos: 4.2f} minuto(s) e {
      segundos} segundo(s) são {segfinal} segundo(s) no total!')
