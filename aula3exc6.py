# Escreva um programa que determine se um número é primo
# ou não.

num = int(input())

if num > 1:
    primo = True

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print('Eh primo')
    else:
        print('Nao eh primo')
else:
    print('Nao eh primo')
