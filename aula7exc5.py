# 5) Conversor de Moeda

def converter_moeda(valor, taxa=5.70):
    convertido = valor * taxa
    texto = f"USD {valor:.2f} → R$ {convertido:.2f}"
    return convertido, texto


valor_convertido, mensagem = converter_moeda(100)
print(mensagem)
