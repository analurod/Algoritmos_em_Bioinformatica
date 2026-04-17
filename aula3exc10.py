# Escreva uma função que recebe como input um número α e,
# através de um loop, aproxima o valor da constante e tal que o erro
# na estimativa é menor que α.
# função deve exibir o valor da constante e com 8 casas decimais e
# exibir também o n necessário na aproximação.

def aproxima_e(alpha):
    soma = 1.0  # primeiro termo (n=0)
    termo = 1.0
    n = 1

    while termo >= alpha:
        termo = termo / n
        soma += termo
        n += 1

    print(f"Valor de e ≈ {soma:.8f}")
    print(f"n necessário: {n-1}")


num = float(input())
aproxima_e(num)
