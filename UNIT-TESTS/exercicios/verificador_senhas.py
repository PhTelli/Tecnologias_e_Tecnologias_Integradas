import re

def verificar_seguranca_senha(senha):
    # Verificar comprimento mínimo
    if len(senha) < 8:
        return False
    
    # Verificar uso de caracteres maiúsculos, minúsculos e especiais
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'[!@#$%^&*()_+{}|:"<>?]', senha):
        return False
    
    return True

