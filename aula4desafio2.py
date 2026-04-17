# Lista 04 - Exercício 2

def limpar_cpf(cpf):
    return "".join([c for c in cpf if c.isdigit()])


def validar_basico(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        return False, "CPF deve ter 11 dígitos"

    if cpf == cpf[0] * 11:
        return False, "Todos os dígitos são iguais"

    return True, "Formato básico válido"


def formatar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        return "Erro: CPF inválido"

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def calcular_digito(cpf_parcial, pesos):
    soma = sum(int(dig) * peso for dig, peso in zip(cpf_parcial, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def validar_completo(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    # Primeiro dígito
    pesos1 = list(range(10, 1, -1))
    dig1 = calcular_digito(cpf[:9], pesos1)

    # Segundo dígito
    pesos2 = list(range(11, 1, -1))
    dig2 = calcular_digito(cpf[:9] + str(dig1), pesos2)

    return cpf[-2:] == f"{dig1}{dig2}"


cpf = input("Digite o CPF: ")

# Validação básica
valido, msg = validar_basico(cpf)
print(msg)

# Formatação
print("CPF formatado:", formatar_cpf(cpf))

# Validação completa
if validar_completo(cpf):
    print("CPF válido (com dígitos verificadores)")
else:
    print("CPF inválido (dígitos verificadores incorretos)")
