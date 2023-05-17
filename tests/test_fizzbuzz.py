import unittest
from fizzbuzz import fizzbuzz


class TestFizz(unittest.TestCase):
    def test_should_return_fizz(self):
        num= 9
        expected_value = "Fizz"
        self.assertEqual(fizzbuzz(num),expected_value)

    def test_should_return_buzz(self):
        num=25
        expected_value = "Buzz"
        self.assertEqual(fizzbuzz(num),expected_value)

    def test_should_return_fizzbuzz(self):
        num=15
        expected_value = "FizzBuzz"
        self.assertEqual(fizzbuzz(num),expected_value)

    def test_should_return_num(self):
        num=2
        expected_value = num
        self.assertEqual(fizzbuzz(num),expected_value)


if __name__ == "__main__":
    unittest.main()