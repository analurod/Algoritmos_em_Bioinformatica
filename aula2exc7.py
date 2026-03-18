# A partir da sequência "AATGCGTACG", exiba apenas os quatro nucleotídeos
# centrais.

# dna = input("Digite a sequência de DNA: ")
dna = 'AATGCGTACG'
tam = len(dna) - 4
meio = int(tam / 2)

for i in range(meio, meio + 4, 1):
    print(dna[i])
