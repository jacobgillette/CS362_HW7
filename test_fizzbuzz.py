import unittest
import fizzbuzz


class TestCase(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fun(0), "Invalid Input") #should throw an error as it's out of the range of numbers

    def test_fizzbuzz1(self):
        self.assertEqual(fizzbuzz.fun(15), "FizzBuzz") #Should pass the test as 15 is divisible by 3 and 5

    def test_fizzbuzz2(self):
        self.assertEqual(fizzbuzz.fun(98), 98) #Should pass the test and return 98 as 98 is not divisible by 3 or 5

    def test_fizzbuzz3(self):
        self.assertEqual(fizzbuzz.fun(6), "Fizz") #Should pass the test as 6 is divisible by 3

    def test_fizzbuzz4(self):
        self.assertEqual(fizzbuzz.fun(10), "Buzz") #Should pass the test as 10 is divisible by 5

if __name__ == '__main__':
  unittest.main(verbosity=2)
