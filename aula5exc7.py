# 7) Retorna somente os números ímpares usando list comprehension

def filtrar_impares(lista):
    return [num for num in lista if num % 2 != 0]


numeros = [1, 2, 3, 4, 5, 6, 7]
print("Ímpares:", filtrar_impares(numeros))
