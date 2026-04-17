# 1) Classificador de IMC Clínico

def classificar_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    return imc, classificacao


valor_imc, classe = classificar_imc(70, 1.75)
print(f"IMC: {valor_imc:.2f} - {classe}")
