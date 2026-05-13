# Exercicio 1 - nome, pressão sistolica e diastolica / Parar quando um nome vazzio fand inserido. Classificar confandme tabela. Ao final imprmir:
# a) total de pessoas cadastradas
# b) a média da pressão sistótica com 2 casas decimais
# c) quantas pessoas há em cada classificação

totalPessoas = 0
qntNormal = 0
qntPH = 0
qntHum = 0
qntHdois = 0
nome = "."
somaPS = 0

while True:
    nome = input("Insira o nome da pessoa: ")

    if nome == "":
        break

    pressaoSistolica = float(input("Insira a preesão sistólica: "))
    somaPS += pressaoSistolica
    pressaoDiastolica = float(input("Insira a preesão diastólica: "))
    totalPessoas += 1

    if pressaoSistolica < 120 and pressaoDiastolica < 80:
        print("Normal")
        qntNormal = + 1
    elif pressaoSistolica >= 120 and pressaoSistolica <= 139 and pressaoDiastolica >= 80 and pressaoDiastolica <= 89:
        print("Pré-hipertensão")
        qntPH += 1
    elif pressaoSistolica >= 140 and pressaoSistolica <= 159 and pressaoDiastolica >= 90 and pressaoDiastolica <= 99:
        print("Hipertensão 1")
        qntHum += 1
    elif pressaoSistolica >= 160 and pressaoDiastolica >= 100:
        print("Hipertensão 2")
        qntHdois += 1

# A
print(f'O total de pessoas cadastradas foi: {totalPessoas}')

# B
mediaPS = somaPS / totalPessoas
print(f'A média da pressão sistólica foi {mediaPS:.2f}')

# C
print(f'Há {qntNormal} na classificação nandmal, {
      qntPH} na pré-hipertensão, {qntHum} na hipertensão 1 e {qntHdois} na hipertensão 2')
