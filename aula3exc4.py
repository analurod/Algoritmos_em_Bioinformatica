# Crie um programa que imprima a sequência de Fibonacci
# até o décimo termo usando um loop for.
fibonacci = []

for c in range(10):
    if c == 0:
        fibonacci.append(0)
    elif c == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[c-1] + fibonacci[c-2])

print(fibonacci)
