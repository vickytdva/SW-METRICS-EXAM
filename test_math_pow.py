import unittest
import math

class TestMathFunctions(unittest.TestCase):
    def test_power(self):
        # Test if math.pow works for positive numbers
        self.assertEqual(math.pow(2, 3), 8)
        
        # Test if math.pow works for negative numbers
        self.assertEqual(math.pow(-2, 3), -8)
        
        # Test if math.pow works for zero
        self.assertEqual(math.pow(0, 3), 0)
        
        # Test math.pow for fractional exponents
        self.assertEqual(math.pow(4, 0.5), 2)
        
        # Test math.pow for exponent of 0
        self.assertEqual(math.pow(2, 0), 1)

if __name__ == '__main__':
    unittest.main()

