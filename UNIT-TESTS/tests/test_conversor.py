import unittest
from exercicios.conversor import *

class TestConversorMoedas(unittest.TestCase):
    def test_dolar_para_euro(self):
        self.assertAlmostEqual(dolar_para_euro(10, 0.82), 8.2, delta=0.01)

    def test_euro_para_dolar(self):
        self.assertAlmostEqual(euro_para_dolar(10, 1.22), 12.2, delta=0.01)

    def test_real_para_dolar(self):
        self.assertAlmostEqual(real_para_dolar(100, 0.2), 20.0, delta=0.01)

    def test_dolar_para_real(self):
        self.assertAlmostEqual(dolar_para_real(50, 5.0), 250.0, delta=0.01)

