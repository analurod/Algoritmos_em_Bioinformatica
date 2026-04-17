# Lista 04 - Exercício 1

def cifra_cesar(texto, chave):
    resultado = ""

    for char in texto:
        if char.isupper():
            novo = (ord(char) - 65 + chave) % 26 + 65
            resultado += chr(novo)
        elif char.islower():
            novo = (ord(char) - 97 + chave) % 26 + 97
            resultado += chr(novo)
        else:
            resultado += char

    return resultado


def descriptografar(texto, chave):
    return cifra_cesar(texto, -chave)


def quebrar_codigo(texto):
    print("\nTentando todas as chaves:\n")
    for chave in range(1, 26):
        tentativa = descriptografar(texto, chave)
        print(f"Chave {chave}: {tentativa}")


texto = input("Digite a mensagem: ")
chave = int(input("Digite a chave (1-25): "))

criptografado = cifra_cesar(texto, chave)
print("Mensagem criptografada:", criptografado)

opcao = input("\nDeseja tentar quebrar a mensagem? (s/n): ")

if opcao.lower() == "s":
    quebrar_codigo(criptografado)
