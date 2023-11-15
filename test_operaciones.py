import unittest
from operaciones import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(7, 3), 10)
        self.assertEqual(sumar(-5, 8), 3)
        self.assertEqual(sumar(0, 0), 0)

    def test_restar(self):
        self.assertEqual(restar(7, 3), 4)
        self.assertEqual(restar(-5, 8), -13)
        self.assertEqual(restar(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(7, 3), 21)
        self.assertEqual(multiplicar(-5, 8), -40)
        self.assertEqual(multiplicar(0, 5), 0)

    def test_dividir(self):
        self.assertAlmostEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(-10, 2), -5)
        # Aqui incluimos una prueba en la que se divida por 0
        with self.assertRaises(ValueError):
            dividir(7, 0)  # Al dividir por cero se debe lanzar un error

if __name__ == '__main__':
    unittest.main()
