# 7) Verificar se uma chave existe no dicionário

dicionario = {"nome": "Ana", "idade": 20, "curso": "Bioinformática"}
chave = input("Digite a chave que deseja verificar: ")

if chave in dicionario:
    print("A chave existe no dicionário.")
else:
    print("A chave não existe no dicionário.")
