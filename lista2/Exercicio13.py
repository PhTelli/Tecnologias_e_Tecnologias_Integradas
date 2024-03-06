def ler_arquivo(nome_arquivo):
    try:
        
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(nome_arquivo))
        return None
    except Exception as e:
        print("Ocorreu um erro ao tentar ler o arquivo:", e)
        return None

nome_do_arquivo = "exemplo.txt"
conteudo_do_arquivo = ler_arquivo(nome_do_arquivo)

if conteudo_do_arquivo:
    print("Conteúdo do arquivo '{}':".format(nome_do_arquivo))
    print(conteudo_do_arquivo)
