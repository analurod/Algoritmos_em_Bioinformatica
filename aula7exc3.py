# 3) Verificador de Par ou Ímpar

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    return "ímpar"


for n in [1, 2, 7, 10, 13]:
    print(n, "->", par_ou_impar(n))
