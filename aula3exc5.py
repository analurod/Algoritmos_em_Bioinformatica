# Escreva um programa que encontre e imprima todos os
# números primos entre 1 e 100.

for num in range(1, 101):
    if num > 1:
        primo = True

        for i in range(2, num):
            if num % i == 0:  # verifica se o número é divisel por algum número diferente dele e 1
                primo = False
                break

        if primo:
            print(num)
