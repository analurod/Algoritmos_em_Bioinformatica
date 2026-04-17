# 1) Gere um dicionário onde cada chave é um caractere e o valor é a quantidade na frase

frase = input("Digite uma frase: ")
contagem = {}

for caractere in frase:
    if caractere in contagem:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1

print(contagem)
