# 5) Agrupar uma lista de dicionários por uma chave específica

def agrupar_por_chave(lista, chave):
    grupos = {}

    for item in lista:
        valor = item[chave]
        if valor not in grupos:
            grupos[valor] = []
        grupos[valor].append(item)

    return grupos


pessoas = [
    {"nome": "Ana", "cidade": "SP"},
    {"nome": "Bruno", "cidade": "RJ"},
    {"nome": "Carla", "cidade": "SP"}
]

print(agrupar_por_chave(pessoas, "cidade"))
