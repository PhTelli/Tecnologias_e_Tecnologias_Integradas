import re

def validar_senha(senha):
    if len(senha) < 6 or len(senha) > 32:
        return "Senha invalida."

    if not re.search(r"[A-Z]", senha) or not re.search(r"[a-z]", senha) or not re.search(r"[0-9]", senha):
        return "Senha invalida."

    if not senha.isalnum():
        return "Senha invalida."

    return "Senha valida."

# Leitura da entrada e processamento dos casos de teste
while True:
    try:
        senha = input()
        resultado = validar_senha(senha)

        print(resultado)
    except EOFError:
        break