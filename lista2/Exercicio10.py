def calcular_frequencia(texto, palavra):
    frequencia = texto.lower().count(palavra.lower())
    return frequencia

meu_texto = "Este é um texto de exemplo. Exemplo é uma palavra que aparece mais de uma vez neste texto."
minha_palavra = "exemplo"
frequencia_palavra = calcular_frequencia(meu_texto, minha_palavra)
print("A palavra '{}' aparece {} vezes no texto.".format(minha_palavra, frequencia_palavra))
