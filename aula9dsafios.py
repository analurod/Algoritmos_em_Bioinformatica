import json


def ler_fasta(nome_arquivo):
    """
    Lê um arquivo FASTA e armazena em um dicionário com as chaves:
    - descricao
    - seq_DNA
    """
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    descricao = ""
    seq = []

    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue

        if linha.startswith(">"):
            descricao = linha[1:]
        else:
            seq.append(linha.upper())

    dicionario = {
        "descricao": descricao,
        "seq_DNA": "".join(seq)
    }

    return dicionario


def complementar(dna_dict):
    """
    Recebe o dicionário do FASTA e retorna a fita complementar da seq_DNA.
    Saída: string
    """
    mapa = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    seq = dna_dict["seq_DNA"]
    seq_complementar = ""

    for base in seq:
        seq_complementar += mapa.get(base, base)

    return seq_complementar


def transcricao(dna_dict):
    """
    Recebe o dicionário e calcula o mRNA da seq_DNA.
    Adiciona a chave seq_RNA ao próprio dicionário.
    Saída: o próprio dicionário atualizado
    """
    seq = dna_dict["seq_DNA"]
    seq_rna = seq.replace("T", "U")
    dna_dict["seq_RNA"] = seq_rna
    return dna_dict


def freq(dna_dict):
    """
    Calcula as frequências percentuais de A, C, T e G da seq_DNA.
    Imprime os resultados e adiciona as chaves:
    Fa, Fc, Ft, Fg
    ao dicionário.
    """
    seq = dna_dict["seq_DNA"]
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


def compare(dict1, dict2):
    """
    Compara 2 sequências de DNA de dois dicionários.
    Imprime a quantidade de nucleotídeos alterados e as posições das trocas.
    """
    seq1 = dict1["seq_DNA"]
    seq2 = dict2["seq_DNA"]

    tamanho_min = min(len(seq1), len(seq2))
    diferencas = []

    for i in range(tamanho_min):
        if seq1[i] != seq2[i]:
            diferencas.append(i)

    if len(seq1) != len(seq2):
        print("As sequências possuem tamanhos diferentes.")
        print("A comparação foi feita até o menor tamanho comum.")

    print(f"Quantidade de nucleotídeos alterados: {len(diferencas)}")

    if diferencas:
        print("Posições das trocas:")
        for pos in diferencas:
            print(f"Índice {pos}: {seq1[pos]} -> {seq2[pos]}")
    else:
        print("As sequências são idênticas nas posições comparadas.")


def busca_motif(dna_dict, motif):
    """
    Procura todas as ocorrências de um motif na seq_DNA.
    Imprime os índices onde o motif foi encontrado.
    """
    seq = dna_dict["seq_DNA"]
    motif = motif.upper()
    posicoes = []

    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i + len(motif)] == motif:
            posicoes.append(i)

    if posicoes:
        print(f"Motif '{motif}' encontrado nas posições: {posicoes}")
    else:
        print(f"Motif '{motif}' não encontrado na sequência.")


def janela_deslizante(dna_dict, k, passo):
    """
    Percorre a seq_DNA com uma janela deslizante de tamanho k
    e passo definido, calculando o conteúdo GC de cada janela.

    Imprime no formato:
    Posição X: GC = Y%

    Adiciona ao dicionário a chave gc_por_janela com uma lista.
    """
    seq = dna_dict["seq_DNA"]
    resultados = []

    if k <= 0 or passo <= 0:
        print("k e passo devem ser maiores que zero.")
        dna_dict["gc_por_janela"] = resultados
        return dna_dict

    for i in range(0, len(seq) - k + 1, passo):
        janela = seq[i:i + k]
        gc = janela.count("G") + janela.count("C")
        gc_percentual = (gc / k) * 100

        resultados.append({
            "posicao": i,
            "janela": janela,
            "gc_percentual": gc_percentual
        })

        print(f"Posição {i}: GC = {gc_percentual:.2f}%")

    dna_dict["gc_por_janela"] = resultados
    return dna_dict


def salvar_json(dna_dict, nome_arquivo_json):
    """
    Salva o dicionário em um arquivo JSON.
    """
    with open(nome_arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(dna_dict, arquivo, indent=4, ensure_ascii=False)

    print(f"Dicionário salvo em '{nome_arquivo_json}' com sucesso.")


def ler_json(nome_arquivo_json):
    """
    Lê um arquivo JSON e retorna um dicionário.
    """
    with open(nome_arquivo_json, "r", encoding="utf-8") as arquivo:
        dicionario = json.load(arquivo)

    return dicionario


# =========================
# Itens do desafio
# =========================

if __name__ == "__main__":
    # Item 1
    corona = ler_fasta("Corona_genomic.fasta")
    print("Dicionário lido do FASTA:")
    print(corona)

    # Item 2
    comp = complementar(corona)
    print("\nFita complementar:")
    print(comp)

    # Item 3
    transcricao(corona)
    print("\nDicionário após transcrição:")
    print(corona)

    # Item 4
    print("\nFrequências percentuais:")
    freq(corona)

    # Item 5
    seqa = ler_fasta("Seq_a.fasta")
    seqb = ler_fasta("Seq_b.fasta")
    print("\nComparação entre Seqa.fasta e Seqb.fasta:")
    compare(seqa, seqb)

    # Item 6
    print("\nBusca de motif:")
    busca_motif(corona, "ATG")

    # Item 7
    print("\nJanela deslizante:")
    janela_deslizante(corona, k=10, passo=5)

    # Item 8
    print("\nSalvando em JSON:")
    salvar_json(corona, "Corona_genomic.json")

    # Item 9
    print("\nLendo do JSON:")
    novo_dict = ler_json("Corona_genomic.json")
    print(novo_dict)
