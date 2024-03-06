def intersecao_listas(lista1, lista2):
    # Inicializar uma lista vazia para armazenar a interseção
    intersecao = []
    
    # Iterar sobre os elementos da primeira lista
    for elemento in lista1:
        # Verificar se o elemento está presente na segunda lista e ainda não foi adicionado à interseção
        if elemento in lista2 and elemento not in intersecao:
            # Se sim, adicioná-lo à lista de interseção
            intersecao.append(elemento)
    
    # Retornar a lista de interseção
    return intersecao

# Exemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print("Interseção das listas:", intersecao_listas(lista1, lista2))
