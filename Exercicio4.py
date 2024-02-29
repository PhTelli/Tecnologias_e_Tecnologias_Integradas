def contar_ocorrencias(frase, palavra):
    palavras_na_frase = frase.split()
    ocorrencias = 0
    
    for palavra_na_frase in palavras_na_frase:
        if palavra_na_frase == palavra:
            ocorrencias += 1
    return ocorrencias

minha_frase = "Esta é uma frase de exemplo. É uma frase simples para exemplificar."
palavra_procurada = "frase"
print("Número de ocorrências da palavra na frase:", contar_ocorrencias(minha_frase, palavra_procurada))
