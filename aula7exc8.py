# 8) Tabela de Referência de Glicemia

import random


def tabela_glicemia(paciente, n_medicoes=5):
    print(f"Medições de glicemia de {paciente}:")
    for i in range(n_medicoes):
        valor = random.randint(70, 200)
        print(f"Medição {i+1}: {valor} mg/dL")


tabela_glicemia("Ana")
