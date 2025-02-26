import unittest
import math 
from calculator import square_root, factorial, natural_log, power

class TestScientificCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertAlmostEqual(square_root(16), 4.0, places=4)
        self.assertAlmostEqual(square_root(25), 5.0, places=4)
        with self.assertRaises(ValueError):
            square_root(-4)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(1), 0.0, places=4)
        self.assertAlmostEqual(natural_log(math.e), 1.0, places=4)
        with self.assertRaises(ValueError):
            natural_log(0)

    def test_power(self):
        self.assertAlmostEqual(power(2, 3), 8.0, places=4)
        self.assertAlmostEqual(power(5, 0), 1.0, places=4)

if __name__ == '__main__':
    unittest.main()
