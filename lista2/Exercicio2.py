def substituir_letra(string, letra_antiga, letra_nova):
   
    nova_string = string.replace(letra_antiga, letra_nova)
    return nova_string


minha_string = "Olá, mundo! Esta é uma frase de exemplo."
letra_antiga = "a"
letra_nova = "o"
nova_string = substituir_letra(minha_string, letra_antiga, letra_nova)
print("String original:", minha_string)
print("Nova string:", nova_string)
