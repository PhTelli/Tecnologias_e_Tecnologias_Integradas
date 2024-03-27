import re

def validar_email(email):
    # Expressão regular para validar o formato do e-mail
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao_email, email) is not None


