# 8) Aproveitamento de um jogador de futebol

jogador = {}
jogador["nome"] = input("Nome do jogador: ")
partidas = int(input("Quantas partidas ele jogou? "))

gols = []
for i in range(partidas):
    gols_partida = int(input(f"Quantos gols na partida {i+1}? "))
    gols.append(gols_partida)

jogador["gols"] = gols
jogador["total"] = sum(gols)

print(jogador)
