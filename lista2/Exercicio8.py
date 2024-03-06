import random
def embaralhar_lista(lista):
    random.shuffle(lista)


minha_lista = [1, 2, 3, 4, 5]
print("Lista original:", minha_lista)

embaralhar_lista(minha_lista)
print("Lista embaralhada:", minha_lista)
