# 11) Potência Recursiva

def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)


print(potencia(2, 2))
