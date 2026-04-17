# 8) Recebe uma lista de strings e retorna a string mais longa

def maior_string(lista):
    maior = lista[0]
    for palavra in lista:
        if len(palavra) > len(maior):
            maior = palavra
    return maior


palavras = ["ana", "bioinformatica", "python", "sol"]
print("String mais longa:", maior_string(palavras))
