import unittest
import ch3


class TestAdd(unittest.TestCase):
    """
    Test the add function from the ch3 library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = ch3.add(1, 2)
        self.assertEqual(result, 3)


class TestSubtract(unittest.TestCase):
    """
    Test the subtract function from the ch3 library
    """

    def test_subtract_integers(self):
        """
        Test that the subtraction of two integers returns the correct total
        """
        result = ch3.subtract(5, 3)
        self.assertEqual(result, 2)


class TestMultiply(unittest.TestCase):
    """
    Test the multiply function from ch3 library
    """

    def test_multiply_integers(self):
        """
        Test that the multiplication of two integers returns the correct total
        """
        result = ch3.multiply(4, 8)
        self.assertEqual(result, 32)


class TestDivide(unittest.TestCase):
    """
    Test the divide function from the ch3 library
    """

    def test_divide_integers(self):
        """
        Test that the division of two integers returns the correct total
        """
        result = ch3.divide(10, 2)
        self.assertEqual(result, 5)


class TestModulo(unittest.TestCase):
    """
    Test the modulo function from the ch3 library
    """

    def test_modulo_integers(self):
        """
        Test that the modulo of two integers return the correct total
        """
        result = ch3.modulo(3, 2)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
