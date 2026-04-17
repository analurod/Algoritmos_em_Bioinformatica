# 4) Área de Superfície Corporal

def asc_dubois(peso, altura):
    return 0.007184 * (peso ** 0.425) * (altura ** 0.725)


def asc_mosteller(peso, altura):
    return ((peso * altura) / 3600) ** 0.5


# altura em cm nessas fórmulas
print("DuBois:", asc_dubois(70, 175))
print("Mosteller:", asc_mosteller(70, 175))
