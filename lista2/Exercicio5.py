def k_maiores_elementos(lista, k):
    lista_copia = lista[:]
    lista_copia.sort(reverse=True)
    maiores_elementos = lista_copia[:k]
    k_maiores_na_ordem_original = []
    
    for elemento in lista:
        if elemento in maiores_elementos:
            k_maiores_na_ordem_original.append(elemento)
    return k_maiores_na_ordem_original

minha_lista = [5, 9, 3, 7, 2, 8, 4, 6]
k = 3
print("Os", k, "maiores elementos na lista são:", k_maiores_elementos(minha_lista, k))
