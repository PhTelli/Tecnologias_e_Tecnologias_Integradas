import unittest
from exercicios.verificador_senhas import *

class TestVerificadorSenhas(unittest.TestCase):
    def test_senha_curta(self):
        self.assertFalse(verificar_seguranca_senha('Abc@1'))  # Senha com menos de 8 caracteres

    def test_senha_sem_maiuscula(self):
        self.assertFalse(verificar_seguranca_senha('senha@123'))  # Senha sem caracteres maiúsculos

    def test_senha_sem_minuscula(self):
        self.assertFalse(verificar_seguranca_senha('SENHA@123'))  # Senha sem caracteres minúsculos

    def test_senha_sem_especial(self):
        self.assertFalse(verificar_seguranca_senha('Senha123'))  # Senha sem caracteres especiais

    def test_senha_insegura(self):
        self.assertFalse(verificar_seguranca_senha('senha123'))  # Senha sem caracteres maiúsculos, minúsculos ou especiais

    def test_senha_segura(self):
        self.assertTrue(verificar_seguranca_senha('Senha@1234'))  # Senha que atende a todos os critérios


