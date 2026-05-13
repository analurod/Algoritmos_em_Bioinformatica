# Crie uma função cifra_cesar que recebe um frase e um inteiro n e retorna a frase com cada letra deslocada n posições no alfabeto.

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


texto = input("Digite a mensagem: ")
chave = int(input("Digite a chave (1-25): "))

criptografado = cifra_cesar(texto, chave)
print("Mensagem inicial:", texto)
print("Mensagem criptografada:", criptografado)
