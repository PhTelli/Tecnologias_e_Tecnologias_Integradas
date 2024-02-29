def contar_palavras(string):
    palavras = string.split()
    return len(palavras)

minha_string = "Batatinha quando nasce"
print("Número de palavras na string:", contar_palavras(minha_string))
