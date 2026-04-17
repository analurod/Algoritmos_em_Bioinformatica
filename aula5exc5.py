# 5) Quatro notas de 5 alunos, calcular média e contar quantos têm média >= 7

medias = []

for i in range(5):
    print(f"\nAluno {i+1}")
    soma = 0
    for j in range(4):
        nota = float(input(f"Digite a {j+1}ª nota: "))
        soma += nota

    media = soma / 4
    medias.append(media)

aprovados = 0
for media in medias:
    if media >= 7.0:
        aprovados += 1

print("Médias:", medias)
print("Quantidade de alunos com média >= 7.0:", aprovados)
