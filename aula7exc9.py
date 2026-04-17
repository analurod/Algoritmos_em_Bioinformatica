# 9) Validador de Sequência de DNA

def validar_dna(sequencia, comprimento_minimo=10):
    if len(sequencia) < comprimento_minimo:
        return False, "Sequência muito curta."

    if " " in sequencia:
        return False, "Sequência contém espaços."

    validos = {"A", "T", "C", "G"}
    for base in sequencia:
        if base not in validos:
            return False, "Sequência contém caracteres inválidos."

    return True, "Sequência válida."


print(validar_dna("ATCGATCGAA"))
print(validar_dna("ATCG X"))
print(validar_dna("ATCGGATCGXS"))
