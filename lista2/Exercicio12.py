def encontrar_menor_string(lista_strings):
    if not lista_strings:
        return None
    
    menor_string = lista_strings[0]
    for string in lista_strings:
        if len(string) < len(menor_string):
            menor_string = string
    return menor_string

lista_de_strings = ["gato", "cachorro", "elefante", "pássaro", "rato"]
menor_string = encontrar_menor_string(lista_de_strings)
print("Menor string na lista:", menor_string)
