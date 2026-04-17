# Ler duas listas e gerar uma terceira com os elementos das duas primeiras

lista1 = []
lista2 = []

for i in range(5):
    lista1.append(int(input(f"Lista 1 - elemento {i+1}: ")))

for i in range(5):
    lista2.append(int(input(f"Lista 2 - elemento {i+1}: ")))

lista3 = lista1 + lista2
print("Terceira lista:", lista3)
