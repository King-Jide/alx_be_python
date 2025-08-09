import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1),0)
        self.assertEqual(self.calc.add(-5,-5), -10)
        self.assertEqual(self.calc.add(0,0),0)

    def test_subtraction(self):
        """Test the subtraction method with various use cases."""
        self.assertEqual(self.calc.subtract(5,3), 2)
        self.assertEqual(self.calc.subtract(-2,3), -5)
        self.assertEqual(self.calc.subtract(-4,-4), 0)
        self.assertEqual(self.calc.subtract(-2,2), -4)

    def test_multiplication(self):
        """Test the multiplication method with various use casees."""   
        self.assertEqual(self.calc.multiply(2,2), 4)
        self.assertEqual(self.calc.multiply(2,-3), -6)
        self.assertEqual(self.calc.multiply(0,10), 0)
        self.assertEqual(self.calc.multiply(5,-2), -10)

    def test_division(self):
        """Test the division method, including division by zero."""
        self.assertEqual(self.calc.divide(10,2), 5)
        self.assertEqual(self.calc.divide(-9,3), -3)
        self.assertEqual(self.calc.divide(5,2), 2.5)
        self.assertEqual(self.calc.divide(5,0), None)# division by zero

    if __name__ == "__main__":
        unittest.main()




        