# Pegue a sequência "TACGATCGG" e exiba apenas os três últimos
# nucleotídeos.

# dna = input("Digite a sequência de DNA: ")
dna = 'TACGATCGG'
tam = len(dna) - 1

for i in range(tam, tam-3, -1):
    print(dna[i])
