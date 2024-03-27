from exercicios.ordenacao import ordenar_lista


def test_ordenar_lista():
    assert ordenar_lista([3, 1, 2]) == [1, 2, 3]
    assert ordenar_lista([3, 1, 2], ascendente=False) == [3, 2, 1]

test_ordenar_lista()