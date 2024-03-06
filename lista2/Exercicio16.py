import os

def consolidar_arquivos_texto(diretorio, arquivo_destino):
    try:
        with open(arquivo_destino, 'w') as destino:
            for nome_arquivo in os.listdir(diretorio):
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)
                if nome_arquivo.endswith('.txt') and os.path.isfile(caminho_arquivo):
                    with open(caminho_arquivo, 'r') as arquivo:
                        destino.write(arquivo.read() + '\n')
        print("Consolidação concluída. Arquivo consolidado criado:", arquivo_destino)
    except Exception as e:
        print("Ocorreu um erro ao tentar consolidar os arquivos:", e)


diretorio = "/caminho/para/seu/diretorio"  # Substitua pelo caminho do seu diretório
arquivo_destino = "arquivo_consolidado.txt"
consolidar_arquivos_texto(diretorio, arquivo_destino)
