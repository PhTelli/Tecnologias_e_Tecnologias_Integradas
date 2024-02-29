import json

def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            dados = json.load(arquivo_json)
            return dados
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(nome_arquivo))
        return None
    except Exception as e:
        print("Ocorreu um erro ao tentar ler o arquivo JSON:", e)
        return None

nome_do_arquivo = "dados.json"
dados = ler_arquivo_json(nome_do_arquivo)

if dados:
    print("Dados lidos do arquivo JSON:")
    print(dados)
