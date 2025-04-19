import unittest
import main

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(main.sumar(2, 3), 5)

    def test_resta(self):
        self.assertEqual(main.sumar(5, 2), 3)

    def test_multiplicar(self):
        self.assertEqual(main.sumar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(main.sumar(10, 2), 5)     

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            main.dividir(10, 0)    

if __name__ == '__main__':
    unittest.main()