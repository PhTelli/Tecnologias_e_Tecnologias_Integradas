def encontrar_par_soma(lista, soma_desejada):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == soma_desejada:
                pares.append((lista[i], lista[j]))
    return pares

minha_lista = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
soma_desejada = 7
pares_encontrados = encontrar_par_soma(minha_lista, soma_desejada)

if pares_encontrados:
    print("Pares encontrados cuja soma é igual a", soma_desejada, ":")
    for par in pares_encontrados:
        print(par)
else:
    print("Não foram encontrados pares na lista cuja soma seja igual a", soma_desejada)
