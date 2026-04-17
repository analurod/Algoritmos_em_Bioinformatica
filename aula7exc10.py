# 10) Contador Global

total_chamadas = 0


def registrar_operacao(operacao):
    global total_chamadas
    print("Operação realizada:", operacao)
    total_chamadas += 1


registrar_operacao("soma")
registrar_operacao("subtração")
registrar_operacao("divisão")

print("Total de operações realizadas:", total_chamadas)
