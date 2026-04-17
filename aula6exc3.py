# 3) Nome, RA e média final de um aluno + situação segundo regra básica:
# média < 3 -> reprovado
# 3 <= média < 6 -> exame
# média >= 6 -> aprovado

aluno = {}
aluno["nome"] = input("Nome do aluno: ")
aluno["RA"] = input("RA do aluno: ")
aluno["media_final"] = float(input("Média final: "))

media = aluno["media_final"]

if media < 3:
    situacao = "Reprovado"
elif media < 6:
    situacao = "Exame"
else:
    situacao = "Aprovado"

aluno["situacao"] = situacao

print(aluno)
