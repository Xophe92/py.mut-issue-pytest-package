import unittest
from demo import fibonacci as fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fib1(self):
        self.assertEqual(fibonacci(1), 1)
    def test_fib2(self):
        self.assertEqual(fibonacci(2), 2)
    def test_fib4(self):
        self.assertEqual(fibonacci(4), 5)

    def test_fibonacci_zero(self):
      with self.assertRaises(ValueError):
        fibonacci(0)

    def test_fibonacci_negative(self):
      with self.assertRaises(ValueError):
        fibonacci(-1)

    def test_fibonacci_types(self):
        with self.assertRaises(TypeError):
            fibonacci("Bonjour")

        with self.assertRaises(TypeError):
            fibonacci(1.2)

if __name__ == '__main__':
    unittest.main()





