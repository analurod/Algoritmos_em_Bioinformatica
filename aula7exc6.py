# 6) Estatísticas de Sinais Vitais

def analisar_sinais(leituras):
    media = sum(leituras) / len(leituras)
    desvio = max(leituras) - min(leituras)
    maior = max(leituras)
    menor = min(leituras)
    return media, desvio, maior, menor


leituras = [120, 125, 118, 130, 122]
media, desvio, maior, menor = analisar_sinais(leituras)

print("Média:", media)
print("Desvio:", desvio)
print("Maior:", maior)
print("Menor:", menor)
