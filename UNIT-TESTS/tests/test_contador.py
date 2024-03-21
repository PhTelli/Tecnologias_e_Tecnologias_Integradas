from exercicios.contador import contar_palavras

def test_contador_palavras():
    assert contar_palavras("Isso é uma frase de exemplo") == 6
    assert contar_palavras("Apenas uma palavra") == 3

test_contador_palavras()  