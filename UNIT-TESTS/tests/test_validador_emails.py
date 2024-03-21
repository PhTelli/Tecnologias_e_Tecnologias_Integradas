import unittest
from exercicios.validador_emails import *

class TestValidadorEmails(unittest.TestCase):
    def test_email_valido(self):
        self.assertTrue(validar_email('usuario@example.com'))
        self.assertTrue(validar_email('usuario123@example.com'))
        self.assertTrue(validar_email('primeiro.ultimo@example.com'))
        self.assertTrue(validar_email('primeiro.ultimo@subdominio.example.com'))
        self.assertTrue(validar_email('primeiro_ultimo@example.com'))
        self.assertTrue(validar_email('primeiro-ultimo@example.com'))

    def test_email_invalido(self):
        self.assertFalse(validar_email('usuario@.com'))
        self.assertFalse(validar_email('usuario@example'))
        self.assertFalse(validar_email('usuario@examplecom'))
        self.assertFalse(validar_email('usuarioexample.com'))
        self.assertFalse(validar_email('usuario.example.com'))

if __name__ == '__main__':
    unittest.main()