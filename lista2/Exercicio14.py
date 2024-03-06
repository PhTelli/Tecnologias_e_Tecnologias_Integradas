import csv

def ler_arquivo_csv(nome_arquivo):
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            cabecalho = next(leitor_csv)
            dados = []
            for linha in leitor_csv:
                dados.append(linha)
            return cabecalho, dados
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(nome_arquivo))
        return None, None
    except Exception as e:
        print("Ocorreu um erro ao tentar ler o arquivo CSV:", e)
        return None, None

nome_do_arquivo = "dados.csv"
cabecalho, dados = ler_arquivo_csv(nome_do_arquivo)

if cabecalho and dados:
    print("Cabecalho:", cabecalho)
    print("Dados:")
    for linha in dados:
        print(linha)
