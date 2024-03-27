from exercicios.validador import validador

def test_validador_telefone():
    assert validador("(12) 1234-5678") == True
    assert validador("(12) 12345-6789") == True
    assert validador("12 1234-5678") == False
    assert validador("(123) 1234-5678") == False
    assert validador("(12) 12345-678") == False