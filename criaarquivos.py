import os


def criar_arquivos_exercicios(base_path, listas):
    # Garante que a pasta existe
    os.makedirs(base_path, exist_ok=True)

    for lista_num, qtd_exercicios in listas.items():
        for exercicio in range(1, qtd_exercicios + 1):
            nome_arquivo = f"aula{lista_num}exc{exercicio}.py"
            caminho_completo = os.path.join(base_path, nome_arquivo)

            # Conteúdo do arquivo
            conteudo = f"""# Lista {lista_num} - Exercício {exercicio}

def main():
    print("Executando Lista {lista_num} - Exercício {exercicio}")

if __name__ == "__main__":
    main()
"""

            # CRIA o arquivo
            with open(caminho_completo, "w", encoding="utf-8") as f:
                f.write(conteudo)

    print("Arquivos criados com sucesso!")


# Caminho
base_path = r"coloquecaminho"

listas = {
    6: 8,
    7: 12,
    8: 15
}

criar_arquivos_exercicios(base_path, listas)
