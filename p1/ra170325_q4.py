def frequencia_nt(dna_dict):
    """
    Calcula as frequências percentuais de A, C, T e G da seq_DNA.
    Imprime os resultados e adiciona as chaves:
    Fa, Fc, Ft, Fg
    ao dicionário.
    """
    seq = dna_dict["seq_DNA"].upper()
    tamanho = len(seq)

    if tamanho == 0:
        dna_dict["Fa"] = 0
        dna_dict["Fc"] = 0
        dna_dict["Ft"] = 0
        dna_dict["Fg"] = 0
        print("Sequência vazia.")
        return dna_dict

    cont_a = seq.count("A")
    cont_c = seq.count("C")
    cont_t = seq.count("T")
    cont_g = seq.count("G")

    fa = (cont_a / tamanho) * 100
    fc = (cont_c / tamanho) * 100
    ft = (cont_t / tamanho) * 100
    fg = (cont_g / tamanho) * 100

    dna_dict["Fa"] = fa
    dna_dict["Fc"] = fc
    dna_dict["Ft"] = ft
    dna_dict["Fg"] = fg

    print(f"Frequência de A: {fa:.2f}%")
    print(f"Frequência de C: {fc:.2f}%")
    print(f"Frequência de T: {ft:.2f}%")
    print(f"Frequência de G: {fg:.2f}%")

    return dna_dict


sequencia = input("Digite a sequência de DNA: ")

dna_dict = {
    "seq_DNA": sequencia
}

resultado = frequencia_nt(dna_dict)
print(resultado)
