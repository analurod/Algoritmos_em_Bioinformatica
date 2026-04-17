# 4) Cadastro de várias pessoas com IMC em uma lista de dicionários

pessoas = []
qtd = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(qtd):
    print(f"\nPessoa {i+1}")
    pessoa = {}
    pessoa["nome"] = input("Nome: ")
    pessoa["sexo"] = input("Sexo: ")
    pessoa["peso"] = float(input("Peso (kg): "))
    pessoa["altura"] = float(input("Altura (m): "))
    pessoa["imc"] = pessoa["peso"] / (pessoa["altura"] ** 2)

    pessoas.append(pessoa)

peso_total = 0
altura_total = 0
imc_total = 0

for pessoa in pessoas:
    peso_total += pessoa["peso"]
    altura_total += pessoa["altura"]
    imc_total += pessoa["imc"]

print("\nQuantidade de pessoas cadastradas:", len(pessoas))
print("Peso médio:", peso_total / len(pessoas))
print("Altura média:", altura_total / len(pessoas))
print("IMC médio:", imc_total / len(pessoas))
