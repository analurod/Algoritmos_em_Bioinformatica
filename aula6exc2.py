# 2a) Dicionário de frutas e dicionário de compras

frutas = {
    "maçã": 3.50,
    "banana": 2.00,
    "uva": 6.50,
    "pera": 5.00,
    "manga": 7.00
}

compras = {
    "maçã": 2,
    "banana": 5,
    "uva": 1,
    "pera": 3
}

print("Frutas:", frutas)
print("Compras:", compras)

# 2b) Calcule o preço total do carrinho

frutas = {
    "maçã": 3.50,
    "banana": 2.00,
    "uva": 6.50,
    "pera": 5.00,
    "manga": 7.00
}

compras = {
    "maçã": 2,
    "banana": 5,
    "uva": 1,
    "pera": 3
}

total = 0

for fruta, quantidade in compras.items():
    total += frutas[fruta] * quantidade

print(f"Total da compra: R$ {total:.2f}")

# 2c) Remova frutas que custam mais de R$ 5,00

frutas = {
    "maçã": 3.50,
    "banana": 2.00,
    "uva": 6.50,
    "pera": 5.00,
    "manga": 7.00
}

remover = []

for fruta, preco in frutas.items():
    if preco > 5.00:
        remover.append(fruta)

for fruta in remover:
    del frutas[fruta]

print(frutas)
